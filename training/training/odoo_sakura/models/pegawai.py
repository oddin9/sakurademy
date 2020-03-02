from odoo import models, fields, api

class PegawaiModel(models.Model):
    _name = 'toko.pegawai'
    _rec_name = 'combination'


    name = fields.Char(string='ID Pegawai')
    nama = fields.Char(string='Nama Pegawai')
    
    combination = fields.Char(string='Combination', compute='_compute_fields_combination')

    alamat = fields.Text(string='Alamat')
    tahun_masuk = fields.Integer(string='Tahun Masuk')
    indeks_prestasi = fields.Float(string='Indeks Prestasi')
    
    tanggal_lahir = fields.Date(string='Tanggal Lahir')
    waktu_bangun = fields.Datetime(string='Waktu Bangun Tidur')
    gender = fields.Selection(
        selection=[
            ('l', 'Laki-laki'),
            ('p', 'Perempuan'),
            ],
        string='Gender')
    
    is_part_time = fields.Boolean(string='Part Time')


   
    @api.depends('name', 'nama')
    def _compute_fields_combination(self):
        for test in self:
            test.combination = test.name + ' | ' + test.nama
    