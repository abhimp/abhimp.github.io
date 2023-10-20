import PhotoSwipeLightbox from '../PhotoSwipe/photoswipe-lightbox.esm.js';
import PhotoSwipe from '../PhotoSwipe/photoswipe.esm.js';

// Simple fullscreen API
const fullscreenAPI = getFullscreenAPI();

// Create custom container
// which will be stretched to fullscreen.
//
// (we can not use PhotoSwipe root element (.pswp),
//  as it is created only after openPromise is resolved)
//
const pswpContainer = getContainer();

function getFullscreenPromise() {
    // Always resolve promise,
    // as wa want to open lightbox 
    // (no matter if fullscreen is supported or not)
    return new Promise((resolve) => {
        if (!fullscreenAPI || fullscreenAPI.isFullscreen()) {
            // fullscreen API not supported, or already fullscreen
            resolve();
            return;
        }
        
        document.addEventListener(fullscreenAPI.change, (event) => {
            pswpContainer.style.display = 'block';
            // delay to make sure that browser fullscreen animation is finished
            setTimeout(function() {
                resolve();
            }, 300);
        }, { once: true });
        
        fullscreenAPI.request(pswpContainer);
    });
}

// pswpModule: PhotoSwipe
const lightbox = new PhotoSwipeLightbox({
    showHideAnimationType: 'none',
    pswpModule: PhotoSwipe,
    preload: [1,2],
    bgClickAction: "close",
    preloaderDelay: 0,
    // tapAction: 'close',
    openPromise: getFullscreenPromise,
    appendToEl: fullscreenAPI ? pswpContainer : document.body,
});

var images = []
function photoSwipeNumItems(numItems) {
    return images.length
}

function photoSwipeItemData(itemData, index) {
    return images[index];
}

var ChangedHash = false;
var DoNotChangeHash = false;

$(document).ready(function(){
    $("img.travel").each(function(i,ele){
        // console.log(ele, i)
        var origimg = $(ele).attr("origimg")
        if(origimg)
        {
            var imgData = {
                src: origimg, 
                height: parseInt($(ele).attr("data-origheight")), 
                width: parseInt($(ele).attr("data-origwidth")),
                alt: $(ele).attr("alt")
            }
            if($(ele).attr("data-caption")) {
                imgData["splCaption"] = $(ele).attr("data-caption")
            }
            if($(ele).attr("data-lat") && $(ele).attr("data-lng") && $(ele).attr("data-url")) {
                imgData["latlng"] = "<a href=\""+encodeURI($(ele).attr("data-url"))+"\" target=\"_blank\">"
                                    + "GPS: " + $(ele).attr("data-lat")+","+$(ele).attr("data-lng")
                                    + "<\a>"
            }
            // console.log(imgData)
            images.push(imgData)
            $(ele).click(function(){
                lightbox.loadAndOpen(i);
            })
            $(ele).css("cursor", "pointer");
        }
    })
    lightbox.addFilter('numItems', photoSwipeNumItems);
    lightbox.addFilter('itemData', photoSwipeItemData);

    lightbox.on('close', () => {
        pswpContainer.style.display = 'none';
        if (fullscreenAPI && fullscreenAPI.isFullscreen()) {
            fullscreenAPI.exit();
        }
    });
    lightbox.on('uiRegister', function() {
        lightbox.pswp.ui.registerElement({
            name: 'custom-caption',
            order: 9,
            isButton: false,
            appendTo: 'root',
            html: 'Caption text',
            onInit: (el, pswp) => {
                lightbox.pswp.on('change', () => {
                    // const currSlideElement = lightbox.pswp.currSlide.data.alt;
                    let captionHTML = lightbox.pswp.currSlide.data.splCaption;
                    if(!captionHTML)
                        captionHTML = lightbox.pswp.currSlide.data.alt || "";
                    // captionHTML = "<h1>ASdasd</h1>";
                    if (lightbox.pswp.currSlide.data.latlng) {
                        captionHTML += "<br>" + lightbox.pswp.currSlide.data.latlng
                    }
                    if(captionHTML) {
                        el.innerHTML = captionHTML;
                        $(el).css("opacity", 1)
                    } else {
                        $(el).css("opacity", 0)
                    }
                });
            }
        });
    });
    lightbox.init();
})

function getFullscreenAPI() {
    let api;
    let enterFS;
    let exitFS;
    let elementFS;
    let changeEvent;
    let errorEvent;
    
    if (document.documentElement.requestFullscreen) {
        enterFS = 'requestFullscreen';
        exitFS = 'exitFullscreen';
        elementFS = 'fullscreenElement';
        changeEvent = 'fullscreenchange';
        errorEvent = 'fullscreenerror';
    } else if (document.documentElement.webkitRequestFullscreen) {
        enterFS = 'webkitRequestFullscreen';
        exitFS = 'webkitExitFullscreen';
        elementFS = 'webkitFullscreenElement';
        changeEvent = 'webkitfullscreenchange';
        errorEvent = 'webkitfullscreenerror';
    }
    
    if (enterFS) {
        api = {
            request: function (el) {
                if (enterFS === 'webkitRequestFullscreen') {
                    el[enterFS](Element.ALLOW_KEYBOARD_INPUT);
                } else {
                    el[enterFS]();
                }
            },
            
            exit: function () {
                return document[exitFS]();
            },
            
            isFullscreen: function () {
                return document[elementFS];
            },
            
            change: changeEvent,
            error: errorEvent
        };
    }
    
    return api;
};

function getContainer() {
    const pswpContainer = document.createElement('div');
    pswpContainer.style.background = '#000';
    pswpContainer.style.width = '100%';
    pswpContainer.style.height = '100%';
    pswpContainer.style.display = 'none';
    document.body.appendChild(pswpContainer);
    return pswpContainer;
}

function resizeImages() {
    var maxWidth = $("section p:first").width()
}