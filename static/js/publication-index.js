/*
 * Strict
 */

'use strict';

/*
 * Title manager
 */

var Title = {};

Title.init = function(){
    this.strings = $('.pub-item a');

    Title.retitle(this.strings);
};

Title.retitle = function(strs){
    $(strs).each(function(){
        var text = $(this).text(),
            replaced = text.replace(/[\u201C\u201D]/g, '"').replace(/[\u2018\u2019]/g, "'");

        var sp = replaced.split('"'),
            markup = "";

        if(sp.length == 3){
            markup = sp[0] + '<span>"' + sp[1] + '"</span>' + sp[2];
        }else{
            markup = replaced;
        }

        $(this).html(markup);
    });
};
