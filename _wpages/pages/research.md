---
layout: about
title: Research
menutype: about
menu_order: 20
plink: research
---

# Research Work
## Video Streaming

{:.text-justify}
Video Streaming major contributing traffic in the Internet. The YouTube alone serve a billion videos to approx 30million viewers. As more video capable devices are getting connected to the Internet, management of video streaming services are getting more difficult. Here are some problems I am working on.

### PARIMA

{:.text-justify}
With increasing advancements in technologies for capturing 360° videos, advances in streaming such videos have become a popular research topic. However, streaming 360° videos require high bandwidth, thus escalating the need for developing optimized streaming algorithms. Researchers have proposed various methods to tackle the problem, considering the network bandwidth or attempt to predict future viewports in advance. However, most of the existing works either (1) do not consider video contents to predict user viewport, or (2) do not adapt to user preferences dynamically, or (3) require a lot of training data for new videos, thus making them potentially unfit for video streaming purposes. We develop _PARIMA_, a fast and efficient online viewport prediction model that uses past viewports of users along with the trajectories of prime objects as a representative of video content to predict future viewports. We claim that the head movement of a user majorly depends upon the trajectories of the prime objects in the video. We employ a pyramid-based bitrate allocation scheme and perform a comprehensive evaluation of the performance of _PARIMA_. In our evaluation, we show that _PARIMA_ outperforms state-of-the-art approaches, improving the Quality of Experience by over 30% while maintaining a short response time.

### EnDASH

{:.text-justify}
User experience of watching videos in smartphones while travelling is often limited by fast battery drainage. Existing client video players use adaptive bitrate (ABR) streaming through Dynamic Adaptive Streaming over HTTP (DASH) to improve user's Quality of Experience (QoE) while ignoring the energy savings aspect, which has been addressed in our work. In this work, we propose EnDASH - an energy aware wrapper over DASH which minimizes energy consumption without compromising on QoE of users, under mobility. First, we undertake an extensive measurement study using two phones and three service providers to understand the dynamics between energy consumption of smartphones and radio related network parameters. Equipped with this study, the proposed system predicts cellular network throughput from the radio parameters within a finite future time window. The prediction engine captures the effect of associated technology and vertical handovers on throughput, unlike existing works. EnDASH then uses deep reinforcement learning based neural networks to first tune the playback butter length to the average predicted cellular network throughput and then to select an optimal video chunk bitrate. It achieves a near 30% decrease in the maximum energy consumption than state-of-the-art ABR Pensieve algorithm while performing almost at par in QoE.
<br>[Learn more..](https://abhijitmondal.in/EnDASH)

### FLiDASH

{:.text-justify}
Live video broadcasts to particular communities or targeted audiences many-at-a-times indulge a cluster of localities from where the end-users are interested in participating. In this work, we leverage this idea to develop a system called Federated Live Streaming over DASH (FLiDASH) which forms end-users coalitions based on the locality of the network connectivity (like a set of end-users behind a common core-network service gateway). In FLiDASH, the coalition members stream the live data collectively based on a federated adaptive bitrate streaming mechanism where the coalition as a whole decides the optimal bitrate for video streaming and distributes the download overhead among its members. We have thoroughly evaluated FLiDASH in an emulated setup, and observe a 40% improvement in the live streaming QoE with a 20% reduction in the network traffic usage.
<br>[Learn more..](https://dl.acm.org/doi/10.1145/3405672.3405806)

### Study with QUIC

{:.text-justify}
This work provides a thorough analysis of various recent adaptive bitrate streaming (ABR) techniques over Google's QUIC protocol. More specifically, we focus on the recent developments of the ABR techniques using control theoretic and reinforcement learning based approaches, and compare their performances over HTTP/TCP and HTTP/QUIC in terms of a wide range of video quality of experience (QoE) parameters. We observe that these ABR techniques are more compatible with HTTP/TCP compared to HTTP/QUIC, and the features of QUIC demands for new ABR technique which can balance the three fundamental QoE parameters - bitrate, smoothness and re-buffering during a video playback.
<br>[Learn more..](https://ieeexplore.ieee.org/document/9084148)


## Transport protocol

## Viscous

{:.text-justify}
The nature of Internet traffic has changed dramatically within the last few years, where a large volume of traffic is originated from mobile applications (known as apps), web based multimedia streaming, computation offloading like cloud computing and Internet of Things (IoT) etc. These types applications generate multiple parallel short lived end-to-end connections. However, the three major requirements of todays’ end-to-end traffic over the Internet, such as (a) support for mobility of devices, (b) capacity improvement through multi-path end-to-end transmissions, and (c) support for short-lived parallel connections, are not substantiated through the widely-deployed transmission control protocol (TCP). Further, the recent developments of multi-path TCP (MPTCP) as well as User Datagram Protocol (UDP) based Google’s Quick UDP Internet Connections (QUIC) also fail to support all the above three requirements. As a consequence, in this work, we develop a new end-to-end transmission protocol, called Viscous, to support the above three requirements over the Internet. Viscous is developed as a wrapper between the application and the transport layer, that works on top of the UDP and supports end-to-end reliability as well as congestion control while transmitting short-lived flows over multiple end-to-end paths. We introduce a number of novel concepts at Viscous, such as parallel and sequential flow multiplexing, decoupling of flow and congestion control etc. to overcome the problems associated with the current transport protocols. Viscous has been implemented and tested over a variety of environments, and we observe that it can significantly boost up the performance of the end-to-end data transmission compared to TCP, MPTCP and QUIC.
<br>[Learn more..](https://abhijitmondal.in/Viscous/)

<!-- ## Multimedia

{:.text-justify}
Research in multimedia with computer network mainly involved streaming services. Streaming services are gaining popularity every day. Few examples are YouTube, Netflix, Skype. There are three types of online streaming services: 1) On-demand (YouTube), ii) Live (YouTube Live) and iii) Interactive (Skype). These three streaming systems have a different kind of problems. Research problem related to video streaming system can be categorized in two ways in computer networking viewpoint. They are i) media delivery system/protocol ii) traffic pattern analysis. In our research group (CNeRG), Currently, there are few projects going on.
 -->
