/*
 * Strict
 */

'use strict';

/*
 * Viewmode manager
 */

var View = {};

View.init = function(){
    this.buttons = $('.subnav-item button');
    this.views = $('.news-list');

    View.register();
};

View.register = function(){
    $(this.buttons).click(function(){
        if(!$(this).hasClass('sel')){
            View.change(this);
        }
    });
};

View.change = function(btn){
    var cls = $(btn).attr('class'),
        mode = cls.split("btn-")[1];

    $(View.views).each(function(){
        $(this).attr('class', 'news-list ' + mode);
    });

    $(View.buttons).each(function(){
        $(this).removeClass('sel');
    });

    $(btn).addClass('sel');
};
