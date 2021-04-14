# -*- coding: utf-8 -*-
{
    'name': "Travel Umroh",

    'summary': """
        Tugas Besar Design Addons for Travel Umroh""",

    'description': """
        Long description of module's purpose
    """,

    'author': "PT. Arkana Solusi Bisnis , muhamadalfarisy98@gmail.com",
    'website': "http://www.arkana.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts','account','product','stock','mrp','sale','purchase','l10n_id','report_xlsx',],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/res_partner_view.xml',
        'views/paket_perjalanan_view.xml',
        'views/sale_order_view.xml',
        'views/menu.xml',

        'report/report.xml',

        'data/data_ir_sequence.xml',
    ],
    # only loaded in demonstration mode
    'qweb': [
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
