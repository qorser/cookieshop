odoo.define('pos_service_charge.PaymentScreenStatusExtended', function(require){
	'use strict';

	const PaymentScreenStatus = require('point_of_sale.PaymentScreenStatus');
	const PosComponent = require('point_of_sale.PosComponent');
	const Registries = require('point_of_sale.Registries');
	const { Component } = owl;

	const PaymentScreenStatusExtended = (PaymentScreenStatus) =>
		class extends PaymentScreenStatus {
			constructor() {
				super(...arguments);
			}

			get service_charges(){
				let order = this.env.pos.get_order();
				let service_charge    = order ? order.get_service_charge() : 0;
				let total = order ? service_charge + order.get_total_with_tax() : 0;

				return service_charge;
			}

			get subtotal(){
				let order = this.env.pos.get_order();
				let subtotal = order ? order.get_total_without_tax() : 0;
				return subtotal;
			}

			get total(){
				let order = this.env.pos.get_order();
				let service_charge    = order ? order.get_service_charge() : 0;
				let total = order ? service_charge + order.get_total_with_tax() : 0;
				return total;
			}

			get taxes(){
				let order = this.env.pos.get_order();
				var total     = order ? order.get_total_with_tax() : 0;
				var taxes     = order ? total - order.get_total_without_tax() : 0;
				return taxes;
			}


	};

	Registries.Component.extend(PaymentScreenStatus, PaymentScreenStatusExtended);

	return PaymentScreenStatus;

});