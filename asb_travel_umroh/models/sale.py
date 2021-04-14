from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    paket_perjalanan_id = fields.Many2one(comodel_name='paket.perjalanan', 
        string='Travel Package')
    
    @api.onchange('paket_perjalanan_id')
    def _onchange_product_tmpl_id(self):
        for r in self:
            if r.paket_perjalanan_id:
                # removes all existing (previous) value from list
                lines=[(5,0,0)]
                line=self.paket_perjalanan_id.product_id
                vals={
                        'product_id':line.id,
                        'name':line.name,
                    }
                lines.append((0,0,vals))
                r.order_line=lines
                