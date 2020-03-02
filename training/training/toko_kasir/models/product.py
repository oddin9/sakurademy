from odoo import models, fields, api

class ProductModel(models.Model):
    _name = 'toko.product'

    name = fields.Char(string='Nama Produk')
    price_unit = fields.Float(string='Price Unit')