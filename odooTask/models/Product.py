from odoo import models, fields


class Product (models.Model):
    _name = 'supermarket.product'
    _inherit = 'supermarket.productCategory'
    _description = 'Product'
    category = fields.Many2one(comodel_name ='Product_category', ondelete='cascade') ## related = cart
    unit_price = fields.Integer(String = 'unit_price')
    name = fields.Char('Name', required=True)