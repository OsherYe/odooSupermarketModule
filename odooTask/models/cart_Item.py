from oddo import models, fields

class Cart_Item (models.Model):
    _name = 'supermarket.Cart_Item'
    _inherits = {   #cartItem has a cart and has a product
        'supermarket.cart': 'cart',
        'supermarket.product': 'product',
    }
    _description = 'Cart_Item'

    customer = fields.Many2one('supermarket.customer')
    cart = fields.Many2one('supermarket.cart')
    product = fields.Many2one('supermarket.product')
    quantity = fields.Integer()
