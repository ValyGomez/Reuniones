# -*- coding: utf-8 -*-
{
    'name': "Gestión sala de reuniones",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Valeria Gómez",
    'website': "https://www.valeriagomez.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.5',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/reunion_view.xml',
        'views/sala_view.xml',
    ],
    # only loaded in demonstration mode

    'demo': [
        'demo/demo.xml',
    ],
}

