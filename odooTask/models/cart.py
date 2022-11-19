from odoo import models, fields, api

class Cart (models.Model):
    _name = 'supermarket.cart'
    _inherit = 'supermarket.customer'
    _description = 'Cart'

    dateOfCreation = fields.Date(context_today='current time')
    total = fields.Float(compute='_compute_total_amount')

    @api.depends('quantity', "priceForUnit")
    def _compute_total_amount(self):
        for record in self:
            total = record.quantity * record.priceForUnit
            record.total = total
