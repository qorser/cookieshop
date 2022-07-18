odoo.define('top_up_via_pos__ris.pos', function(require) {
	"use strict";

	var models = require('point_of_sale.models');
	var screens = require('point_of_sale.ProductScreen');
	var core = require('web.core');
	const { Gui } = require('point_of_sale.Gui');
	var popups = require('point_of_sale.ConfirmPopup');
	var QWeb = core.qweb;
	var utils = require('web.utils');
	var round_pr = utils.round_precision;
	var _t = core._t;

	var OrderSuper = models.Order;
	models.Order = models.Order.extend({

		init: function(parent, options) {
			var self = this;
			this._super(parent,options);
			this.set_serial_number();
		},
		
		set_serial_number: function(entered_serial_number, phone_number){
			if (!this.serial_number){
				this.serial_number = [{
					'sn' : entered_serial_number,
					'phone' : phone_number
				}]
			}
			else{
				this.serial_number.push({
					'sn' : entered_serial_number,
					'phone' : phone_number
				})
			}
			this.trigger('change',this);
		},

		get_serial_number: function(){
			
			var order = this.pos.get_order();
			if (order) {
				var serial_number = this.serial_number
				return serial_number
			}
		},
		

	});
});