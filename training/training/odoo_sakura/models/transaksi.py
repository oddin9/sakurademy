from odoo import models, fields, api


class TransaksiModel(models.Model):
    _name = 'toko.transaksi'

    name = fields.Char(string='No Nota')
    nama_kasir = fields.Char(string='Nama Kasir')

    pegawai_id = fields.Many2one('toko.pegawai', string='Kasir')

    line_ids = fields.One2many('toko.transaksi_line', 'transaksi_id', string='Detail')

    metode = fields.Boolean(string='Tunai ?')
    ammount = fields.Float(string='Ammout')

    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('confirm', 'Confirm'),
            ('closed', 'Closed'),
            ],
        string='State',default='draft')

    
        
    

    
    