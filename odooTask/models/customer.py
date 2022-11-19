# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Customer(models.Model):
    _name = 'supermarket.customer'
    _description = 'Customer'

    name = fields.Char('Name', required=True)
    email = fields.Char('Email')
    city = fields.Char('City')
    street = fields.Char('Street')
    
    bestSellerItems = fields.Int(compute='_compute_bs')

    def _compute_bs(self):
        for record in self:
            bestSellerSearch = self.env['supermarket.cartItem'].search((['castumerName', '=', record.name]), order='quantity', limit = '3')
            record.bestSellerItems = bestSellerSearch
    
    


    
