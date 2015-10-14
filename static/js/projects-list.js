/*
 * Strict
 */

'use strict';

/*
 * Folder manager
 */

var Folder = {};

Folder.init = function(){
    this.buttons = $('.category-title');

    Folder.register();
};

Folder.register = function(){
    $(this.buttons).on('click', function(){Folder.anchor(this)});
};

Folder.anchor = function(btn){
    var group = $(btn).parent().parent();

    if($(group).hasClass('sel')){
        Folder.fold(group);
    }else{
        Folder.unfold(group);
    }
};

Folder.fold = function(group){
    var projects = $(group).children('.project-wrapper');

    $(projects).stop().slideUp(350, "easeInOutQuad", function(){
        $(group).removeClass('sel');
    });
};

Folder.unfold = function(group){
    var projects = $(group).children('.project-wrapper');

    $(projects).stop().slideDown(350, "easeInOutQuad", function(){
        $(group).addClass('sel');
    });
};
