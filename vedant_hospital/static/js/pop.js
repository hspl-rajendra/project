odoo.define('vedant_hospital.message', function (require) {
"use strict";
    console.log('sunil madhad')
    var FormController = require('web.FormController');

    var ExtendFormController = FormController.include({
        saveRecord:function(){
            console.log('Contact Saved!')
            var res = this._super.apply(this, arguments);
            if(this.modelName == 'hospital.appointment'){
                this.do_notify('Success', 'Record Saved!');
            }
            return res;
        }
    })
});


