from odoo import models, fields


class ProductCategory (models.Model):
    _name = 'supermarket.productCategory'
    _description = 'ProductCategory'

    name = fields.Char('Name')
