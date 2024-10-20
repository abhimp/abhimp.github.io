---
layout: blog
title: Openssl and single threaded application
menutype: blog
menu_order: 20
plink: asyncOpenSSL
---

## OpenSSL

OpenSSL is one of the greatest opensource tool we have. It is used by many project as it is defacto tool for SSL based solutions.

The best thing about OpenSSL is that it is platform agonastic and ease of use. Writing portable code is so much easier with OpenSSL.

Also OpenSSL support different kind of IOs and very easy adapt a new one if it does exists already. It also support both blocking and non-blocking IO operation. The blocking IO operation is easy and simple. OpenSSL would wait until underlying operation ends. It works out of the box, easy and simple. However, it needs system threads to handle each side of a connection which could be wastfull. The non-blocking IO is little involving and have several caveates.

### OpenSSL with non-blocking IO
Non-blocking IO is a way to working to multiple IOs from a single thread. Here, IO operations wont block if it can perform the operation rather return with appropriate notification. So, program can perform opertaion in loop. However this method causes wasting CPU spining. So, the defacto standard is to use some method to get notification about the possibily of available operation on IOs. The implementation of such tool is platform dependent and beyond the scope of this documentation. However, such tools works on the system IOs not on the application level IOs.

So, such notification mechanism are not capable of polling OpenSSL. So, to use OpenSSL, with non-blocking IOs, we have to use the notification mechanism on Non-Blocking IOs and translate them corresponding SSL connection.

Lets see how can we read data from SSL connection using non-blocking IOs.

```c
#include <openssl/ssl.h>
#include <openssl/err.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/select.h>

int non_blocking_ssl_read(SSL *ssl, int fd, char *buf, int buf_size) {
    int ret;
    fd_set readfds;

    // Set the file descriptor to non-blocking
    int flags = fcntl(fd, F_GETFL, 0);
    fcntl(fd, F_SETFL, flags | O_NONBLOCK);

    while (1) {
        FD_ZERO(&readfds);
        FD_SET(fd, &readfds);

        // Wait for the socket to be readable
        ret = select(fd + 1, &readfds, NULL, NULL, NULL);

        if (ret < 0) {
            perror("select");
            return -1;
        } else if (FD_ISSET(fd, &readfds)) {
            // Try to read from the SSL connection
            ret = SSL_read(ssl, buf, buf_size);
            
            if (ret > 0) {
                // Successfully read data
                printf("Read %d bytes from SSL connection\n", ret);
                return ret;
            } else {
                int ssl_error = SSL_get_error(ssl, ret);
                if (ssl_error == SSL_ERROR_WANT_READ || ssl_error == SSL_ERROR_WANT_WRITE) {
                    // SSL wants to retry the read or write operation
                    continue;
                } else {
                    // Some other error occurred
                    fprintf(stderr, "SSL_read error: %d\n", ssl_error);
                    return -1;
                }
            }
        }
    }
}
```

This solution above looks ok. It also works fine most of the cases. However there is a caveate.

#### The caveat
Lets assume a scenerio. The sender sends 2048bytes over the SSL connection, then it expects some output from the other end. The receiver side receives only 1048bytes at a time.

In this particular scenerio.

