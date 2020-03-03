from odoo import models, fields, api

class TransaksiLineModel(models.Model):
    _name = 'toko.transaksi_line'
    _rec_name = 'transaksi_id'


    produk_id = fields.Many2one('toko.product', string='Nama Produk')
    price_unit = fields.Float(string='Price Unit', compute='_get_price', store=True)
    quantity = fields.Integer(string='Quantity')
    total_harga = fields.Float(compute='_compute_total', string='Total', store=True)
    transaksi_id = fields.Many2one('toko.transaksi', string='Header')
    
    @api.depends('quantity','price_unit')
    def _compute_total(self):
        for data in self:
            data.total_harga = data.price_unit * data.quantity


    @api.depends('produk_id')
    def _get_price(self):
        for udin in self:
            udin.price_unit= udin.produk_id.price_unit
    
