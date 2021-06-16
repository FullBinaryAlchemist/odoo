{
    'name': 'Real Estate Application',
    'version': '1.0',
    'category': 'Sales',
    'depends': ['base','web'],
    'data' : [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True
}