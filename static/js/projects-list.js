/*
 * Strict
 */

'use strict';

/*
 * Image manager
 */

var Image = {};

Image.init = function(){
    this.buttons = $('.image-expand');

    Image.register();
};

Image.register = function(){
    $(Image.buttons).click(function(){
        Image.folder(this);
    });
};

Image.folder = function(obj){
    if($(obj).hasClass('opened')){
        $(obj).removeClass('opened');
        Image.close(obj);
    }else{
        $(obj).addClass('opened');
        Image.open(obj);
    }
};

Image.open = function(obj){
    //animate button
    var deco_l = $(obj).children('.image-expand-left'),
        deco_r = $(obj).children('.image-expand-right');

    $(deco_l).stop().animate({
        left: "+=8"
    }, 300);

    $(deco_r).stop().animate({
        right: "+=8"
    }, 300);

    //animate image box
    var image = $(obj).parent().children('img'),
        wrapper = $(obj).parent();

    var height = $(image).height();

    $(image).stop().animate({
        marginTop: "0px"
    }, 300);

    $(wrapper).stop().animate({
        height: height
    }, 300);
};

Image.close = function(obj){
    //animate button
    var deco_l = $(obj).children('.image-expand-left'),
        deco_r = $(obj).children('.image-expand-right');

    $(deco_l).stop().animate({
        left: "-=8"
    }, 300);

    $(deco_r).stop().animate({
        right: "-=8"
    }, 300);

    //animate image box
    var image = $(obj).parent().children('img'),
        wrapper = $(obj).parent();

    $(image).stop().animate({
        marginTop: "-160px"
    }, 300);

    $(wrapper).stop().animate({
        height: "120px"
    }, 300);
};

/*
 * Detail manager
 */

var Detail = {};

Detail.init = function(){
    this.buttons = $('.research-more');

    Detail.register();
};

Detail.register = function(){
    $(Detail.buttons).click(function(){
        Detail.folder(this);
    });
};

Detail.folder = function(obj){
    if($(obj).hasClass('opened')){
        $(obj).removeClass('opened');
        Detail.close(obj);
    }else{
        $(obj).addClass('opened');
        Detail.open(obj);
    }
};

Detail.open = function(obj){
    // change wording
    $(obj).text("Hide Details");

    // animate details box
    var section = $(obj).parent().children('.research-details'),
        wrapper = $(obj).parent();

    $(section).stop().slideDown(500);
    $(wrapper).animate({
        marginTop: "10px",
        marginBottom: "10px",
        backgroundColor: "#f5f5f5"
    }, 300);
};

Detail.close = function(obj){
    // change wording
    $(obj).text("See Details");

    // animate details box
    var section = $(obj).parent().children('.research-details'),
        wrapper = $(obj).parent();

    $(section).stop().slideUp(500);
    $(wrapper).animate({
        marginTop: "0px",
        marginBottom: "0px",
        backgroundColor: "#fff"
    }, 300);
};

/*
 * Video manager
 */

var Video = {};

Video.init = function(){
    this.videos = $('iframe[src^="http://www.youtube.com"]');

    Video.resize();
};

Video.resize = function(){
    $(Video.videos).each(function(){
        console.log($(this).width(), $(this).height());
    });
};
