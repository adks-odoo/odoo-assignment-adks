from odoo import models,fields

class StockTransportDoc(models.Model):
    _name = "stock.transport.dock"
    _rec_name = 'dock'

    dock = fields.Char(required=True)
