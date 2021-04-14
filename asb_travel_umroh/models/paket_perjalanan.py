from odoo import api, fields, models
from odoo.exceptions import UserError,ValidationError
from datetime import date

class PaketPerjalanan(models.Model):
    _name = 'paket.perjalanan'
    _description = 'Paket Perjalanan'

    name = fields.Char(string='', required=True, copy=False, readonly=True,
                            default='New')
    company_id = fields.Many2one('res.company', string='Company', 
        default=lambda self: self.env.user.company_id)
    currency_id = fields.Many2one('res.currency', string='Currency', 
        related='company_id.currency_id')
    departure_date = fields.Date(string='Departure Date',required=True)
    return_date = fields.Date(string='Return Date',required=True)
    product_tmpl_id = fields.Many2one(comodel_name='mrp.bom', 
        string='Package',required=True)
    product_id = fields.Many2one(comodel_name='product.template', 
        string='Sale',required=True)
    quota = fields.Integer(string='Quota')
    remaining_seats = fields.Integer(string='Remaining Seats',
        compute='_get_remaining_seats',store=True,readonly=True)
    quota_progress = fields.Float(string='Quota Progress',compute='_get_quota_progress')
    state = fields.Selection(string='Status', selection=[
        ('draft', 'Draft'), ('confirmed', 'Confirmed'),
        ('done', 'Done')],default='draft')
    paket_hotel_line = fields.One2many(comodel_name='paket.hotel.line', inverse_name='paket_perjalanan_id', 
        string='Hotel Lines')   
    paket_pesawat_line = fields.One2many(comodel_name='paket.pesawat.line', inverse_name='paket_perjalanan_id', 
        string='Airline Lines')
    paket_acara_line = fields.One2many(comodel_name='paket.acara.line', inverse_name='paket_perjalanan_id', 
        string='Schedule Lines')
    hpp_line = fields.One2many(comodel_name='hpp.line', inverse_name='paket_perjalanan_id', string='hpp Lines')
    paket_peserta_line = fields.One2many(comodel_name='paket.peserta.line', inverse_name='paket_perjalanan_id', 
        string='Manifest')
    
    note= fields.Text(string='Note')
    amount_total = fields.Monetary(string='Total', store=True, readonly=True, 
        compute='_amount_all',)
    
    
    @api.model
    def create(self, vals):
        """
        create student id sequence 
        """
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'paket.perjalanan.sequence') or 'New'
        result = super(PaketPerjalanan, self).create(vals)
        return result
    
    @api.depends('paket_peserta_line','quota')
    def _get_remaining_seats(self):
        for r in self:
            if not r.quota:
                r.remaining_seats=0
            else:
                r.remaining_seats=r.quota-len(r.paket_peserta_line)

    @api.depends('paket_peserta_line','quota')
    def _get_quota_progress(self):
        for r in self:
            if not r.quota:
                r.quota_progress=0
            else:
                r.quota_progress=(len(r.paket_peserta_line)/ r.quota)*100


    @api.onchange('quota')
    def _onchange_quota(self):
        if self.quota<0:
            raise ValidationError('Tidak bisa kurang dari 0')
        if self.quota<len(self.paket_peserta_line):
            raise ValidationError("Increase min Quota or remove excess Jamaah")
    
    @api.onchange('product_tmpl_id')
    def _onchange_product_tmpl_id(self):
        for r in self:
            if r.product_tmpl_id:
                # removes all existing (previous) value from list
                lines=[(5,0,0)]
                for line in self.product_tmpl_id.bom_line_ids:
                    vals={
                        'product_id':line.product_id.id,
                        'product_qty':line.product_qty
                    }
                    lines.append((0,0,vals))
                r.hpp_line=lines

    @api.depends('hpp_line.subtotal','hpp_line')
    def _amount_all(self):
        """
        Compute the total amounts.
        """
        for r in self:
            amount_count =0.0
            for line in r.hpp_line:
                amount_count += line.subtotal
            r.amount_total=amount_count

    def name_get(self):
        '''Method to display name and code'''
        return [(r.id, r.name + '# '+r.product_id.name) for r in self]

    def button_action_confirm(self):
        for r in self:
            r.write({'state': 'confirmed'})

    def button_action_set_to_draft(self):
        for r in self:
            r.write({'state': 'draft'})

    def button_action_done(self):
        for r in self:
            r.write({'state': 'done'})

    def button_update_jamaah(self):
        '''Method to update manifest line by searching SO with same paket perjalanan id'''
        for r in self:
            return True

class PaketHotelLine(models.Model):
    _name = 'paket.hotel.line'
    _description = 'Paket Hotel Line'

    name = fields.Many2one(comodel_name='res.partner', string='Hotel',
        domain="[('is_hotel','=',True)]",required=True)
    start_date = fields.Date(string='Start Date',required=True)
    end_date = fields.Date(string='End Date',required=True)
    city = fields.Char(string='City',related='name.city',readonly=1)
    paket_perjalanan_id = fields.Many2one(comodel_name='paket.perjalanan', 
        string='Paket Perjalanan')
    
class PaketPesawatLine(models.Model):
    _name = 'paket.pesawat.line'
    _description = 'Paket Hotel Line'

    name = fields.Many2one(comodel_name='res.partner', string='Pesawat',
        domain="[('is_airline','=',True)]",required=True)
    departure_date = fields.Date(string='Departure Date',required=True)
    departure_city = fields.Char(string='Departure City',required=True)
    arrival_city = fields.Char(string='Arrival City',required=True)
    paket_perjalanan_id = fields.Many2one(comodel_name='paket.perjalanan', 
        string='Paket Perjalanan')

class PaketAcaraLine(models.Model):
    _name = 'paket.acara.line'
    _description = 'Paket Acara Line'

    name = fields.Char(string='Name')
    date = fields.Date(string='Date')
    paket_perjalanan_id = fields.Many2one(comodel_name='paket.perjalanan', 
        string='Paket Perjalanan')
    
class HppLine(models.Model):
    _name = 'hpp.line'
    _description = 'Paket perjalanan Line'

    product_id = fields.Many2one(comodel_name='product.product', string='Product')
    product_qty = fields.Integer(string='Quantity')
    price_subtotal = fields.Float(string='Price')
    subtotal = fields.Float(string='Subtotal',compute='_get_subtotal',store=True,readonly=True)
    paket_perjalanan_id = fields.Many2one(comodel_name='paket.perjalanan', string='Paket perjalanan')
    

    @api.depends('price_subtotal','product_qty')
    def _get_subtotal(self):
        for r in self:
            if r.price_subtotal==0:
                r.subtotal=0
            else:
                r.subtotal=r.price_subtotal*r.product_qty


    @api.onchange('price_subtotal')
    def _onchange_price_subtotal(self):
        if self.price_subtotal<0:
            raise ValidationError('Tidak bisa kurang dari 0')
    
class PaketPesertaLine(models.Model):
    _name = 'paket.peserta.line'
    _description = 'Paket Peserta Line'
    _inherits = {'res.partner': 'jamaah_id'}

    paket_perjalanan_id = fields.Many2one(comodel_name='paket.perjalanan', string='Paket perjalanan')
    jamaah_id = fields.Many2one(comodel_name='res.partner', string='Jamaah',
        domain="[('is_customer', '=', True)]")
    room_type = fields.Selection(string='Room Type', help='Paket kamar',required=True,
        selection=[('quad', 'Quad'), ('double', 'Double'),('triple', 'Triple')],default='quad')
    age = fields.Integer(string='Age',compute='_get_age_jamaah',store=True)
    mahram_ids = fields.Many2many(comodel_name='res.partner', string='Mahram',
        domain="[('is_customer', '=', True)]")
    note = fields.Text(string='Notes')

    @api.depends('birthdate')
    def _get_age_jamaah(self):
        '''Method to calculate age'''
        current_dt = date.today()
        for rec in self:
            if rec.birthdate:
                start = rec.birthdate
                age_calc = ((current_dt - start).days / 365)
                # Age should be greater than 0
                if age_calc > 0.0:
                    rec.age = age_calc
            else:
                rec.age = 0

    
    

    