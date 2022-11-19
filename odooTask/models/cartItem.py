from oddo import models, fields


class CartItem (models.Model):
    _name = 'supermarket.cartItem'
    _inherits = {
        'supermarket.cart': 'cart',
        'supermarket.product': 'product',
    }
    _description = 'CartItem'

    customer = fields.Many2one('supermarket.customer')
    cart = fields.Many2one('supermarket.cart')
    product = fields.Many2one('supermarket.product')
    quantity = fields.Integer()
    amount = fields.Float(compute='_compute_total')
