{
    'name': "dispatch management system",
    'version': '1.0',
    'depends': ['stock_picking_batch','fleet'],
    'category':'Stock Transport',
    'data': ['security/ir.model.access.csv',
             'views/stock_transport_fleet_views.xml',
             'views/stock_transport_inventory_views.xml'],
    'installable': True,
    'application': True,
}
