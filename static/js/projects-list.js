/*
 * Strict
 */

'use strict';

/*
 * Folder manager
 */

var Folder = {};

Folder.init = function(){
    this.buttons = $('.research-title');

    Folder.register();
};

Folder.register = function(){
    $(this.buttons).on('click', function(){Folder.anchor(this)});
};

Folder.anchor = function(btn){
    var wrapper = $(btn).parent(),
        details = $(wrapper).children('.research-details');

    if($(btn).hasClass('selected')){
        Folder.fold(details, btn);
    }else{
        Folder.unfold(details, btn);
    }
};

Folder.fold = function(details, btn){
    $(details).stop().slideUp(350, "easeInOutQuad", function(){
        $(btn).removeClass('selected');
        $(btn).parent().removeClass('selected');
    });
};

Folder.unfold = function(details, btn){
    $(details).stop().slideDown(350, "easeInOutQuad", function(){
        $(btn).addClass('selected');
        $(btn).parent().addClass('selected');
    });
};
