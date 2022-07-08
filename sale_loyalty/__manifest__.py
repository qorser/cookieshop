# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).

{
    'name': 'Sale Loyalty',
    'version': '15.0.1.1',
    'category': 'Sales/Sales',
    'summary': 'Customers can get rewards option with Discount, Voucher, and Gift, by Loyalty Program Rules then the customer can spend those points to get rewards on purchasing.',
    'description': """
        - Loyalty Points and Rewards on Sale Order
        - Redeem points as per customer requirement
        - Gift the product base on reward rules
        - Give Discount to customer based on the customer loyalty points and based on reward rule
    """,
    'license': 'OPL-1',
    'author': 'Kanak Infosystems LLP.',
    'website': 'https://www.kanakinfosystems.com',
    'depends': ['sale_management','membership'],
    'data': [
        'security/sale_loyalty_security.xml',
        'security/ir.model.access.csv',
        'data/sale_loyalty_data.xml',
        'views/sale_loyalty_views.xml',
        'views/res_config_view.xml',
        'views/sale_view.xml',
        'views/sale_portal_template.xml',
        'views/sale_loyalty_history_views.xml',
        'views/res_partner.xml',
        'report/sale_report.xml',
        'report/points_history_report.xml',
        'wizard/point_selection_wizard_view.xml'
    ],
    'images': ['static/description/banner.jpg'],
    'sequence': 1,
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 50,
    'currency': 'EUR'
}
