from odoo import fields, models,api

class StockTransportFleet(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.max_weight} kg, {record.max_volume} m3)"
