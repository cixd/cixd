/*
 * Strict
 */

'use strict';

/*
 * Photo booth slider
 */

var PhotoBooth = {};

PhotoBooth.init = function(){
    this.prev = $('.photo-list-prev');
    this.next = $('.photo-list-next');

    $(this.prev).hide();
    PhotoBooth.register();
};

PhotoBooth.register = function(){
    $(this.prev).on('click', PhotoBooth.prevPage);
    $(this.next).on('click', PhotoBooth.nextPage);
};

PhotoBooth.prevPage = function(){
    PhotoBooth.slider(-1);
};

PhotoBooth.nextPage = function(){
    PhotoBooth.slider(1);
};

PhotoBooth.slider = function(dir){
    $(PhotoBooth.prev).off('click', PhotoBooth.prevPage);
    $(PhotoBooth.next).off('click', PhotoBooth.nextPage);

    var list = $('.photo-list'),
        items = $('.photo-item'),
        limit = $(list).width() * ($(items).length - 1) * (-1);

    var moveto = $(list).position().left - ($(list).width() * dir);

    if(moveto > 0 || moveto < limit){
        return;
    }else{
        $(PhotoBooth.prev).show();
        $(PhotoBooth.next).show();
    }

    if(moveto == 0){
        $(PhotoBooth.prev).hide();
    }else if(moveto == limit){
        $(PhotoBooth.next).hide();
    }

    $(list).animate({
        'left': moveto + "px"
    }, 500, function(){
        $(PhotoBooth.prev).on('click', PhotoBooth.prevPage);
        $(PhotoBooth.next).on('click', PhotoBooth.nextPage);
    });
};

/*
 * News slider
 */

var News = {};

News.init = function(){
    this.prev = $('.news-list-prev');
    this.next = $('.news-list-next');

    $(this.prev).hide();
    News.register();
};

News.register = function(){
    $(this.prev).on('click', News.prevPage);
    $(this.next).on('click', News.nextPage);
};

News.prevPage = function(){
    News.slider(-1);
};

News.nextPage = function(){
    News.slider(1);
};

News.slider = function(dir){
    $(News.prev).off('click', News.prevPage);
    $(News.next).off('click', News.nextPage);

    var list = $('.news-list'),
        items = $('.news-item'),
        items_l = items.length,
        limit = ($(items[0]).width() + 30) * (items_l - 3) + ($(list).width() * 0.2),
        limit = limit * -1;

    console.log($(items[0]).width());

    var moveto = $(list).position().left - ($(list).width() * dir);

    if($(list).position().left == 0 || $(list).position().left == limit){
        moveto = $(list).position().left - ($(list).width() * 0.7 * dir);
    }

    console.log(moveto, limit);

    if(moveto > 0){
        moveto = 0;
    }else if(moveto < limit){
        moveto = limit;
    }else{
        $(News.prev).show();
        $(News.next).show();
    }

    if(moveto == 0){
        $(News.prev).hide();
    }else if(moveto == limit){
        $(News.next).hide();
    }

    $(list).animate({
        'left': moveto + "px"
    }, 500, function(){
        $(News.prev).on('click', News.prevPage);
        $(News.next).on('click', News.nextPage);
    });
};
