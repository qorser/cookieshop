odoo.define('top_up_via_pos__ris.PosIsiPulsaWidget', function(require) {
    "use strict";

    const ProductScreen = require('point_of_sale.ProductScreen');
    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
    const ajax = require('web.ajax');

    // Start PosBagWidget
    class PosIsiPulsaWidget extends PosComponent {
        constructor() {
            super(...arguments);
        }

        renderElement (){
            var self = this;
            self.showPopup('PosIsiPulsaPopupWidget', {});

        }
    };
    PosIsiPulsaWidget.template = 'PosIsiPulsaWidget';

    Registries.Component.add(PosIsiPulsaWidget);

    return PosIsiPulsaWidget;

});
