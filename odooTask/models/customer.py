# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Customer(models.Model):
    _name = 'supermarket.customer'
    _description = 'Customer'

    name = fields.Char('Name', required=True)
    email = fields.Char('Email')
    city = fields.Char('City')
    street = fields.Char('Street')
    
    most_freq_item = fields.Int(compute='_compute_bs')
    discount_val = fields.Float(compute= '_apply_discount')
    total = fields.Float(compute ='_apply_discount')
    
    ## discount on best seller product
    @api.depends('value', 'discount')
    def _compute_bs(self):
        for record in self:
            the_item = self.env['supermarket.cartItem'].search((['Name', '=', record.name]), order='quantity', limit = '4')
            record.most_freq_item = the_item
        discount = the_item * discount
        the_item.discount_val = discount
        the_item.total = the_item - discount
        
    
    


    
