from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    paket_perjalanan_id = fields.Many2one(comodel_name='paket.perjalanan', 
        string='Travel Package')
    
