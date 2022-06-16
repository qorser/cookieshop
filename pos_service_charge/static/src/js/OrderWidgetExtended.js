odoo.define('pos_service_charge.OrderSummaryExtended', function(require){
	'use strict';

	const OrderSummary = require('point_of_sale.OrderSummary');
	const PosComponent = require('point_of_sale.PosComponent');
	const Registries = require('point_of_sale.Registries');
	const { Component } = owl;

	const OrderSummaryExtended = (OrderSummary) =>
		class extends OrderSummary {
			constructor() {
				super(...arguments);
			}
			get service_charges(){
				let order = this.env.pos.get_order();
				let service_charge    = order ? order.get_service_charge() : 0;
				let total = order ? service_charge + order.get_total_with_tax() : 0;
				return service_charge.toFixed(2);
			}
			get subtotal(){
				let order = this.env.pos.get_order();
				let subtotal = order ? order.get_total_without_tax() : 0;
				return subtotal.toFixed(2);
			}
			get total(){
				let order = this.env.pos.get_order();
				let service_charge    = order ? order.get_service_charge() : 0;
				let total = order ? service_charge + order.get_total_with_tax() : 0;
				return total.toFixed(2);
			}
			get taxes(){
				let order = this.env.pos.get_order();
				var total = order ? order.get_total_with_tax() : 0;
				var taxes = order ? total - order.get_total_without_tax() : 0;
				return taxes.toFixed(2);
			}
	};

	Registries.Component.extend(OrderSummary, OrderSummaryExtended);

	return OrderSummary;

});
