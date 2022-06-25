# -*- coding: utf-8 -*-
{
    'name': "top_up_via_pos_RIS",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            '/top_up_via_pos__ris/static/src/js/isi_pulsa.js',
            '/top_up_via_pos__ris/static/src/js/isi_pulsa_popup_widget.js',
            '/top_up_via_pos__ris/static/src/css/customer_facing_display_top_up.css',
        ],
        'web.assets_qweb': [
            '/top_up_via_pos__ris/static/src/xml/isi_pulsa.xml',
            '/top_up_via_pos__ris/static/src/xml/receipt.xml'
        ],
        # 'web.assets_frontend': [
        #     '/top_up_via_pos__ris/static/src/css/customer_facing_display_top_up.css',
        # ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
