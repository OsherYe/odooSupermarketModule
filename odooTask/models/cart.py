from odoo import models, fields, api

class Cart (models.Model):
    _name = 'supermarket.cart'
    _inherit = 'supermarket.customer'
    _description = 'Cart'

    date = fields.Date(context_today='current time')
    total = fields.Float(compute='_compute_total_amount')

    @api.depends('quantity', 'unit_price')
    def _compute_total_amount(self):
        for record in self:
            total = record.quantity * record.unit_price
            record.total = total
