from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    lang_id = fields.Many2one(comodel_name='res.lang', string='Language')
    is_hotel = fields.Boolean(string='Is a Hotel')
    is_airline = fields.Boolean(string='Is a Airline')
    is_customer = fields.Boolean(string='Is a Customer')
    is_vendor = fields.Boolean(string='Is a Vendor')
    
    #Additional Information
    no_ktp = fields.Char(string='KTP No')
    father_name = fields.Char(string='Father\'s Name')
    mother_name = fields.Char(string='Mother\'s Name')
    birthdate = fields.Date(string='Date of Birth')
    place_of_birth = fields.Char(string='Place of Birth')
    job = fields.Char(string='Job')
    marital_status = fields.Selection(string='Marital Status', 
        selection=[('single', 'Single'), ('married', 'Married'),
        ('divorce', 'Divorce'),])
    gender = fields.Selection(string='Gender', 
        selection=[('man', 'Man'), ('woman', 'Woman'),])
    blood_type = fields.Selection(string='Blood Type', 
        selection=[('a', 'A'), ('ab', 'AB'),
        ('b', 'B'),('o', 'O')])
    education = fields.Selection(string='Education', 
        selection=[('sd', 'SD'), ('smp', 'SMP'),
            ('sma', 'SMA'),('diploma', 'Diploma'),
            ('s1', 'S1'),('s2', 'S2'),('s3', 'S3')])
    clothes_size = fields.Selection(string='Clothes Size', 
        selection=[('xs', 'XS'), ('s', 'S'),
        ('m', 'M'), ('l', 'L'),
        ('xl', 'XL'), ('xxl', 'XXL'),
        ('xxxl', 'XXXL'), ('4l', '4L'),])
    
    #Passport information
    no_passport = fields.Char(string='Passport No')
    date_expired = fields.Date(string='Date of Expired')
    date_issued = fields.Date(string='Date Issued')
    name_passport = fields.Char(string='Passport Name')
    imigrasi = fields.Char(string='Imigrasi')

    #Scan Document
    passport = fields.Image(string='Passport')
    ktp = fields.Image(string='KTP')
    buku_nikah = fields.Image(string='Buku Nikah/ Akta Lahir')
    kartu_keluarga = fields.Image(string='Kartu Keluarga')
    
    
    
    
    
    
    
    
    
    
    
    
