odoo.define('top_up_via_pos__ris.PosIsiPulsaPopupWidget', function(require) {
    "use strict";

    const Popup = require('point_of_sale.ConfirmPopup');
    const Registries = require('point_of_sale.Registries');
    const PosComponent = require('point_of_sale.PosComponent');
    const OrderReceipt = require('point_of_sale.OrderReceipt')
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
            var product_code_input = document.querySelector('[name="product_code"]').value
            var phone_input = document.querySelector('[name="phone"]').value
            var IRS_type_input = document.querySelector('[name="IRS_type"]').value
            var trx_id = PosComponent.env.pos.get_order().uid

            ajax.jsonRpc('/isipulsa', 'call', {
                'phone': phone_input, 
                'id' : IRS_id_input,
                'pin' : IRS_pin_input,
                'kode' : product_code_input,
                'trx_id': trx_id, 
                'trx_type' : IRS_type_input, 

            })
            .then(function (result) { 
                setTimeout(function(){ 
                    alert(result)
                    // DI SINI UNTUK MENAMBAHKAN NOMOR HP DAN NOMOR SN
                    PosComponent.env.pos.set({
                        'phone': phone_input,
                        'sn':  '123457',
                    });
                }, 3000);
               
                }
            )

            this.showScreen('ProductScreen');
            this.trigger('close-popup');
        }
    };
    PosIsiPulsaPopupWidget.template = 'PosIsiPulsaPopupWidget';

    Registries.Component.add(PosIsiPulsaPopupWidget);

    return PosIsiPulsaPopupWidget;
});
