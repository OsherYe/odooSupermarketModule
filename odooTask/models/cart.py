from odoo import models, fields, api

class Cart (models.Model):
    _name = 'supermarket.cart'
    _inherit = 'supermarket.customer'
    _description = 'Cart'

    date = fields.Date(context_today='current time')
    total = fields.Float(compute='_compute_total_amount')
    twice = fields.Boolean(compute='_compute_if_twice')
    time_in_super = fields.Datetime('YYYY-MM-DD HH:MM:SS')
    update_time = fields.Datetime('YYYY-MM-DD HH:MM:SS')
    total_amount = fields.Integer(compute='_compute_total_amount')
    
    @api.depends('quantity', 'unit_price')
    def _compute_total_amount(self):
        for record in self:
            total = record.quantity * record.unit_price
            record.total = total
    
    @api.depends('customer', 'time_in_super')
    def _compute_if_twice(self):
        last_occ = self.time_in_super
        for record in self:
            if (record.check_out - last_occ < 8 ): return True 
        return False  
