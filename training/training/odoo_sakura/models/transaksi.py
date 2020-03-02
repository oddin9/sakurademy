from odoo import models, fields, api


class TransaksiModel(models.Model):
    _name = 'toko.transaksi'

    name = fields.Char(string='No Nota')
    nama_kasir = fields.Char(string='Nama Kasir')

    pegawai_id = fields.Many2one('toko.pegawai', string='Kasir')

    produk = fields.Char(string='Nama Produk')

    produk_id = fields.Many2one('toko.product', string='Produk')
    

    qty = fields.Integer(string='Qty')
    harga = fields.Float(string='Harga',readonly=True, compute='get_harga',store=True)
    total = fields.Float(string='Total', readonly=True, compute='get_price_total', store=True)

    @api.depends('qty', 'harga')
    def get_price_total(self):
        self.total = self.qty * self.harga
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'test',
                'type': 'rainbow_man',
            }
        }

    @api.depends('produk_id')
    def get_harga(self):
        for test in self:
            test.harga = test.produk_id.price_unit

  
    

    
    