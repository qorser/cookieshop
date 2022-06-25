odoo.define('top_up_via_pos__ris.PosIsiPulsaPopupWidget', function(require) {
    "use strict";

    const Popup = require('point_of_sale.ConfirmPopup');
    const Registries = require('point_of_sale.Registries');
    const PosComponent = require('point_of_sale.PosComponent');
    const ajax = require('web.ajax');

    class PosIsiPulsaPopupWidget extends Popup {
        constructor() {
            super(...arguments);
        }

        go_back_screen() {
            this.showScreen('ProductScreen');
            this.trigger('close-popup');
        }
        isi_pulsa() {
            var IRS_id_input = document.querySelector('[name="IRS_id"]').value
            var IRS_pin_input = document.querySelector('[name="IRS_pin"]').value
            var IRS_user_input = document.querySelector('[name="IRS_user"]').value
            var IRS_password_input = document.querySelector('[name="IRS_password"]').value
            var product_code_input = document.querySelector('[name="product_code"]').value
            var phone_input = document.querySelector('[name="phone"]').value
            var IRS_trx_id_input = document.querySelector('[name="IRS_trx_id"]').value
            var IRS_type_input = document.querySelector('[name="IRS_type"]').value

            console.log(IRS_id_input)
            console.log(IRS_pin_input)
            console.log(IRS_user_input)
            console.log(IRS_password_input)
            console.log(product_code_input)
            console.log(phone_input)
            console.log(IRS_trx_id_input)
            console.log(IRS_type_input)

            ajax.jsonRpc('/isipulsa', 'call', {
                'phone': phone_input
            })
            .then(function (result) { 
                // console.log(result)
                setTimeout(function(){ 
                    console.log('Pengisian berhasil!')
                    alert(result)
                }, 3000);
               
                }
            )

            // setTimeout(function(){ 
            //     console.log('Pengisian berhasil!')
            //     alert('Pengisian pulsa berhasil!')
            // }, 3000);
            this.showScreen('ProductScreen');
            this.trigger('close-popup');
        }
    };
    PosIsiPulsaPopupWidget.template = 'PosIsiPulsaPopupWidget';

    Registries.Component.add(PosIsiPulsaPopupWidget);

    return PosIsiPulsaPopupWidget;
});
