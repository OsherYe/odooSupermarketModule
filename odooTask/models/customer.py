# -*- coding: utf-8 -*-
from odoo import fields, models


class Customer(models.Model):
    _name = 'supermarket.customer'
    _description = 'Customer'

    name = fields.Char('Name', required=True)
    email = fields.Char('Email')
    city = fields.Char('City')
    street = fields.Char('Street')
    
    most_freq_item = fields.Int(compute='_compute_item_most_freq')
    discount_val = fields.Float(compute= '_compute_item_most_freq')
    total = fields.Float(compute ='_compute_item_most_freq')
    check_out = fields.Datetime('YYYY-MM-DD HH:MM:SS')
    
    ## discount on best seller product
    @api.depends('discount')
    def _compute_item_most_freq(self):
        for record in self:
            the_item = self.env['supermarket.cartItem'].search((['Name', '=', record.name]), order='quantity', limit = '4')
            record.most_freq_item = the_item
        discount = the_item * discount
        the_item.discount_val = discount
        the_item.total = the_item - discount
        
    premium_customer = fields.Boolean(compute='_compute_custumers_appear')

    @api.depends('cart.customer', 'cart.twice') #use compute info from other Module table.
    def _compute_custumers_appear(self):
       return (self.cart.twice)
        
    
    


    
