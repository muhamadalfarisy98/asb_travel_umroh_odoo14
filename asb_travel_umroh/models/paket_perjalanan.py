from odoo import api, fields, models
from odoo.exceptions import UserError,ValidationError


class PaketPerjalanan(models.Model):
    _name = 'paket.perjalanan'
    _description = 'Paket Perjalanan'

    name = fields.Char(string='', required=True, copy=False, readonly=True,
                            default='New')
    departure_date = fields.Date(string='Departure Date',required=True)
    return_date = fields.Date(string='Return Date',required=True)
    product_tmpl_id = fields.Many2one(comodel_name='mrp.bom', string='Package',required=True)
    product_id = fields.Many2one(comodel_name='product.template', string='Sale',required=True)
    quota = fields.Integer(string='Quota')
    remaining_seats = fields.Integer(string='Remaining Seats',
        compute='_get_remaining_seats')
    quota_progress = fields.Float(string='Quota Progress')
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
    
    note= fields.Text(string='Note')
    

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
    
    @api.depends('paket_pesawat_line','quota')
    def _get_remaining_seats(self):
        for r in self:
            if not r.quota:
                r.remaining_seats=0
            else:
                r.remaining_seats=r.quota-len(r.paket_pesawat_line)

    @api.onchange('quota')
    def _onchange_quota(self):
        if self.quota<0:
            raise ValidationError('Tidak bisa kurang dari 0')
        if self.quota<len(self.paket_pesawat_line):
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

    def name_get(self):
        '''Method to display name and code'''
        return [(rec.id, rec.name + '# '+rec.product_id.name) for rec in self]


class PaketHotelLine(models.Model):
    _name = 'paket.hotel.line'
    _description = 'Paket Hotel Line'

    name = fields.Many2one(comodel_name='res.partner', string='Hotel',
        domain="[('is_hotel','=',True)]")
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
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
    price = fields.Float(string='Price')
    subtotal = fields.Float(string='Subtotal')
    paket_perjalanan_id = fields.Many2one(comodel_name='paket.perjalanan', string='Paket perjalanan')
    
    
    
    
    