{
    'name': "transport management",
    'version': '1.0',
    'depends': ['base','mail','stock'],
    'category':'Transport Management',
    'data': ['security/ir.model.access.csv',
             'views/stock_transport_fleet_views.xml',
             'views/stock_transport_fleet_category_views.xml',
             'views/stock_transport_inventory_views.xml'],
    'installable': True,
    'application': True,
}
