from odoo import fields, models,api

class StockTransportInventory(models.Model):
    _inherit = 'stock.picking.batch'

    vehicle = fields.Many2one('fleet.vehicle',string='Vehicle')
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category',string='Vehicle Category')
    weight = fields.Float(compute="_compute_weight_bar")
    volume = fields.Float(compute="_compute_volume_bar")

    @api.depends('vehicle_category_id', 'move_line_ids')
    def _compute_weight_bar(self):
        for batch in self.picking_ids:
            print(batch.move_line_ids)
        for record in self:
            if(record.vehicle_category_id):
                product_weight = 0
                for products in record.move_line_ids:
                    product_weight += products.product_id.weight * products.quantity
                record.weight = (product_weight / record.vehicle_category_id.max_weight) * 100
            else:
                record.weight = 0.0

    @api.depends('vehicle_category_id', 'move_line_ids')
    def _compute_volume_bar(self):
        for record in self:
            if(record.vehicle_category_id):
                product_volume = 0
                for products in record.move_line_ids:
                    product_volume += products.product_id.volume * products.quantity
                record.volume = (product_volume / record.vehicle_category_id.max_volume) * 100
            else:
                record.volume = 0.0
