odoo.define('top_up_via_pos__ris.PosIsiPulsaPopupWidget', function(require) {
    "use strict";

    const Popup = require('point_of_sale.ConfirmPopup');
    const Registries = require('point_of_sale.Registries');
    const PosComponent = require('point_of_sale.PosComponent');
    const OrderReceipt = require('point_of_sale.OrderReceipt')
    const ajax = require('web.ajax');
    const NumberBuffer = require('point_of_sale.NumberBuffer');
    var rpc = require('web.rpc');

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
            var pos_number = PosComponent.env.pos.get_order().uid
            // var id_trx = document.querySelector('[name="id_trx"]').value
            var counter = document.querySelector('[name="counter"]').value


            let order = this.env.pos.get_order()
            var top_up_list = order.get_serial_number()
            if (top_up_list){
                var counter = top_up_list.length+1
                var trx_id = pos_number+"("+counter+")"
            }
            else{
                var trx_id = pos_number+"(1)"
            }            

            ajax.jsonRpc('/isipulsa', 'call', {
                'phone': phone_input, 
                'id' : IRS_id_input,
                'pin' : IRS_pin_input,
                'kode' : product_code_input,
                'trx_id': trx_id, 
                // 'trx_id': id_trx, 
                'counter': counter,
                'trx_type' : IRS_type_input,

            })
            .then(function (result) { 
                setTimeout(function(){ 
                    var res = JSON.stringify(result)
                    console.log(result)
                    //MENAMBAHKAN PRODUK SAAT BERHASIL MENGISI
                    var res_json = JSON.parse(res)
                    if (res_json.success === true){
                        if ((res_json.rc === '0068' || res_json.rc === '68' || res_json.rc === '0027' || res_json.rc === '1'){
                            alert(res_json.msg+ ". ID Transaksi: " + res_json.reffid)
                            // DI SINI UNTUK MENAMBAHKAN NOMOR HP DAN NOMOR SN
                            order.set_serial_number(res_json['sn'], res_json['tujuan'])

                            
                            //MENEMUKAN PRODUK DENGAN KODE YANG DIMASUKKAN
                            var model = 'product.product';
                            var domain = [['default_code', '=', product_code_input]];
                            var fields = [];
                            rpc.query({
                                model: model,
                                method: 'search_read',
                                args: [domain, fields],
                            }).then(function (data) {
                                const product = PosComponent.env.pos.db.get_product_by_id(data[0].id);
                                const added_product = order.add_product(product);
                                NumberBuffer.reset();
                            });
                        }
                    }
                    else{
                        alert("Pengisian gagal. " + res_json.msg+ ". ID Transaksi: " + res_json.reffid)
                    }
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
