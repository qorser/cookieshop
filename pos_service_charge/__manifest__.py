# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name": "POS Service Charge in odoo",
    "version": "15.0.0.1",
    "category": "Point of Sale",
    "depends": ['point_of_sale'],
    "author": "BrowseInfo",
    'summary': 'Apply service charges on POS order charges pos services charge pos charges service point of sales service charges pos extra charges pos additional pos charges service tax pos service tax pos tax service charges POS service management all on one pos service',
    "description": """
    
    Purpose :-
    Odoo POS Service Charges point of sale service charges point of sales
    odoo pos service tax pos charges pos extra charges
    odoo apply service charge on POS apply service charge on point of sale
    odoo apply service charges on POS apply service charges on point of sale
    odoo pos charge based from a percentage POS fixed service charge
    odoo point of sale charge based from a percentage point of sale fixed service charge


    Odoo Point of Sale Service Charges point of sales service charges POS
    odoo Point of Sale service tax Point of Sale charges Point of Sale extra charges
    odoo apply service charge on Point of Sale apply service charge on POS
    odoo apply service charges on Point of Sale apply service charges on POS
    odoo Point of Sale charge based from a percentage Point of Sale fixed service charge Point of Sale
    odoo POS charge based from a percentage POS fixed service charge Point of Sale


    Odoo Point of Sales Service Charges point of sale service charges on POS
    odoo Point of Sales service tax Point of Sales charges Point of Sale extra charges on POS
    odoo apply service charge on Point of Sales apply service charge point of sales
    odoo apply service charges on Point of Sales apply service charges on point of sales
    odoo Point of Sales charge based from a percentage Point of Sales fixed service charge Point of Sales
    odoo point of sales charge based from a percentage point of sales fixed service charge Point of Sales


    """,
    "price": 19,
    "currency": 'EUR',
    "website": "https://www.browseinfo.in",
    "data": [
        'views/custom_pos_view.xml',
        'data/data.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_service_charge/static/src/js/pos.js',
            'pos_service_charge/static/src/js/ServiceChargeButton.js',
            'pos_service_charge/static/src/js/OrderWidgetExtended.js',
            'pos_service_charge/static/src/js/PaymentScreenStatus.js',
        ],
        'web.assets_qweb': [
            'pos_service_charge/static/src/xml/**/*',
        ],
    },
    "auto_install": False,
    "installable": True,
    "images": ['static/description/Banner.png'],
    "live_test_url": 'https://youtu.be/xbpgg3tVmzk',
    'license': 'OPL-1',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
