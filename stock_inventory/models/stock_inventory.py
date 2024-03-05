from odoo import fields, models

class ResConfig(models.TransientModel):
    _inherit = 'res.config.settings'

    module_stock_transport = fields.Boolean('Dispatch Management System')
