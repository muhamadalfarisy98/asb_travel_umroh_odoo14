# -*- coding: utf-8 -*-
{
    'name': "Travel Umroh",

    'summary': """
        Tugas Besar Design Addons for Travel Umroh""",

    'description': """
        Long description of module's purpose
    """,

    'author': "PT. Arkana Solusi Bisnis , muhamadalfarisy98@gmail.com",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts','account','product','stock','mrp','sale','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/res_partner_view.xml',
        'views/menu.xml',
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
