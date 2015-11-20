/*
 * Strict
 */

'use strict';

/*
 * Popup manager
 */

var Popup = {};

Popup.init = function(){
    this.box = $('.sec-popup');
    this.text = $('.popup-content');
    this.buttons = $('.topic-show');

    Popup.register();
};

Popup.register = function(){
    $(this.buttons).hover(
        function(){
            Popup.show(this);
        },
        function(){
            Popup.hide();
        }
    );
};

Popup.show = function(trigger){
    var content = $(trigger).parent().find('.topic-content').text();

    $(Popup.box).css({
        top: $(trigger).position().top + 36
    });

    $(Popup.text).text(content);
    $(Popup.box).fadeIn('fast');
};

Popup.hide = function(){
    $(Popup.box).fadeOut('fast');
};
