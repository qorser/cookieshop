odoo.define('pos_service_charge.ServiceChargeButton', function(require) {
	'use strict';

	const PosComponent = require('point_of_sale.PosComponent');
	const ProductScreen = require('point_of_sale.ProductScreen');
	const { useListener } = require('web.custom_hooks');
	const Registries = require('point_of_sale.Registries');

	class ServiceChargeButton extends PosComponent {
		constructor() {
			super(...arguments);
			useListener('click', this.onClick);
		}
		async onClick() {
			let order = this.env.pos.get_order();
			let self = this;
			if (order.orderlines.length === 0) {
				this.showPopup('ErrorPopup', {
					title: this.env._t('Service charge type is not slected'),
					body: this.env._t('Please select service charge type in pos configuration.'),
				});
			}
			else
			{
				if (this.env.pos.config.service_charge_type === false) {
					this.showPopup('ErrorPopup', {
						title: this.env._t('Service charge type is not slected'),
						body: this.env._t('Please select service charge type in pos configuration.'),
					});
				}
				else
				{
					const { confirmed, payload: inputNumber } = await this.showPopup('NumberPopup', {
						startingValue: 0,
						title: this.env._t('Service Charges'),
					});
					let service_charge = inputNumber !== ""? Math.abs(inputNumber): null;
					if (confirmed && service_charge !== null) {
						order.set_service_charge(service_charge);
					}
				}
			}
		}
	}
	ServiceChargeButton.template = 'ServiceChargeButton';

	ProductScreen.addControlButton({
		component: ServiceChargeButton,
		condition: function() {
			return this.env.pos.config.service_charge_type;
		},
	});

	Registries.Component.add(ServiceChargeButton);

	return ServiceChargeButton;
});


