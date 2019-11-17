odoo.define('module.extension_name', function (require) {
    'use strict';
    var ajax =  require('web.ajax');
    require('web.dom_ready');
    var core = require('web.core');
    var FormView = require('web.FormView');
    var _t = core._t;
    var Qweb= core.qweb;
    FormView.include({
        load_record: function(record) {
        // disable only for cancel and paid account.invoice
        if (record){
            if (this.model == 'student.student' & _.contains(['dismiss'], record.state)){
                    $('button.oe_form_button_edit').hide()
                }else {
                    $('button.oe_form_button_edit').hide()
                }
        }
        // call super
        return this._super(record);
        }
    });
    // FormView.include({
    //  load_record: function() {
    //   this._super.apply(this, arguments);
    //   if (this.model === 'student.student') {
    //       if (this.datarecord && (this.datarecord.state === 'dismiss')) {
    //         this.$buttons.find('.o_form_button_edit').css({'display':'none'});
    //       }
    //       else {
    //         this.$buttons.find('.o_form_button_edit').css({'display':''});
    //       }
    //    }
    // }});

$(document).ready(function () {
    console.log('test click test');
    $('body').on('click','.reload_page_js',function () {
        console.log('test click');
    });

});
});

