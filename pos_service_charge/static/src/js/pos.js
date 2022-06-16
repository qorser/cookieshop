odoo.define('pos_service_charge.pos', function(require) {
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
			this.set_service_charge();
		},
		
		set_service_charge: function(entered_charge){
			this.service_charge = entered_charge;
			this.trigger('change',this);
		},

		get_service_charge: function(){
			
			var utils = require('web.utils');
			var round_pr = utils.round_precision;
			var rounding = this.pos.currency.rounding;
			var percentage_charge = 0;
		   
			var order = this.pos.get_order();
			if (order) {
			
				if (this.pos.config.service_charge_type === 'fixed') {
				
					var service = this.service_charge;
					var percentage_charge = service;
					return round_pr(percentage_charge, rounding);
				}
				else if (this.pos.config.service_charge_type === 'percentage') {
					var order = this.pos.get_order();
					var subtotal = order.get_total_without_tax();
					var service = this.service_charge;
					var percentage = (subtotal * service) /100;
					var percentage_charge = percentage;
					return round_pr(percentage_charge, rounding);
				}
				else{
					return 0.0;
				}
			}
		},

		get_change: function(paymentline) {
			var utils = require('web.utils');
			var round_pr = utils.round_precision;
			var rounding = this.pos.currency.rounding;
			if (!paymentline) {
				var change = this.get_total_paid() - (this.get_total_with_tax() + this.get_service_charge());
			} else {
				var change = -(this.get_total_with_tax() + this.get_service_charge()); 
				var lines  = this.paymentlines.models;
				for (var i = 0; i < lines.length; i++) {
					change += lines[i].get_amount();
					if (lines[i] === paymentline) {
						break;
					}
				}
			}
			return round_pr(Math.max(0,change), this.pos.currency.rounding);
		},

		get_due: function(paymentline) {
			if (!paymentline) {
				var due = this.get_total_with_tax() - this.get_total_paid() + this.get_service_charge();
			}
			else {
				var due = this.get_total_with_tax() + this.get_service_charge();
				var lines = this.paymentlines.models;
				for (var i = 0; i < lines.length; i++) {
					if (lines[i] === paymentline) {
						break;
					} else {
						due -= lines[i].get_amount();
					}
				}
			}
			return round_pr(due, this.pos.currency.rounding);
		},
	
		export_as_JSON: function() {
			var self = this;
			var loaded = OrderSuper.prototype.export_as_JSON.call(this);
			loaded.service_charge = self.get_service_charge();
			loaded.amount_total = self.get_service_charge() + self.get_total_with_tax();
			return loaded;
		},

		init_from_JSON: function(json){
			OrderSuper.prototype.init_from_JSON.apply(this,arguments);
			this.service_charge = json.service_charge | 0.0;
			this.amount_total = json.amount_total || 0.0;
		},
	
	});
});
