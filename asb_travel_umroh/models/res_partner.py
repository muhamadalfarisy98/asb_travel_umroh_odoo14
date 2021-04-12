from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_hotel = fields.Boolean(string='Is a Hotel')
    is_airline = fields.Boolean(string='Is a Airline')
    
    
