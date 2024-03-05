from odoo import models,fields

class StockTransportFleet(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Float(string='Max Weight(kg)')
    max_volume = fields.Float(string='Max Volume(m3)')

    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.max_weight} kg, {record.max_volume} m3)"
