from odoo import api, fields, models

class StockPicking(models.Model):
    _inherit= "stock.picking"

    weight= fields.Float(compute= "_compute_weight_vol", default =0, store= True)
    volume = fields.Float(compute = "_compute_weight_vol", default =0, store= True)

    @api.depends("move_ids")
    def _compute_weight_vol(self):
        for record in self:
            total_weight = 0
            total_volume = 0
            for move in record.move_ids:
                total_weight += move.product_id.weight * move.quantity
                total_volume += move.product_id.volume * move.quantity
            record.weight = total_weight
            record.volume = total_volume
