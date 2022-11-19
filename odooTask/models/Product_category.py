from odoo import models, fields


class Product_category (models.Model):
    _name = 'supermarket.productCategory'
    _description = 'ProductCategory'

    name = fields.Char('Name')
