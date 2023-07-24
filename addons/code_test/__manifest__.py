{
    'name' : 'Odoo Code Test',
    'version' : '14.0.1.0.0',
    'depends' : [
        'base',
        'crm',
        'stock',
        'sale',
        'sale_management',
        'account',
        'mrp',
    ],
    'data': [
        'views/assets.xml',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': False,
}
