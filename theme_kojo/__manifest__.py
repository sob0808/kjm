# -*- coding: utf-8 -*-
{
    'name': "Kojo's Motor Theme",

    'summary': """Kojo's Motor Theme""",

    'description': """
        Kojo's Motor Theme
    """,

    'author': "SOB",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Theme/Hidden',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', "website_sale", "theme_default"],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        "templates/layout.xml",
        'views/views.xml',
        'views/assets.xml',
        'views/snippets.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}