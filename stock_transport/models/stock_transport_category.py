from odoo import fields, models

class InheritCategory(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Float(string='Max Weight(kg)')
    max_volume = fields.Float(string='Max Volume(m3)')
