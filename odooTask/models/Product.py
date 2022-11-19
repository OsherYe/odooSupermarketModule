from models.productCategory import ProductCategory
from odoo import models, fields


class Product (models.Model):
    _name = 'supermarket.product'
    _inherit = 'supermarket.productCategory'
    _description = 'Product'
    category = fields.Many2one(comodel_name ='Category', ondelete='cascade')
    unit_price = fields.Integer(String = 'Unit Price')
    name = fields.Char('Name', required=True)