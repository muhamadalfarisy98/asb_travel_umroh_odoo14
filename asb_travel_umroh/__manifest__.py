# -*- coding: utf-8 -*-
{
    'name': "Travel Umroh",

    'summary': """
        Tugas Akhir Design Addons for Travel Umroh""",

    'description': """
        Long description of module's purpose
    """,

    'author': "PT. Arkana Solusi Bisnis , <muhamad alfarisy> muhamadalfarisy98@gmail.com",
    'website': "http://www.arkana.co.id",
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
        'views/account_move_view.xml',
        'views/stock_picking_view.xml',
        'views/menu.xml',

        'report/report.xml',
        'report/customer_invoice_template.xml',
        'report/stock_picking_template.xml',

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
