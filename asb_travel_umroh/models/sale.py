from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    paket_perjalanan_id = fields.Many2one(comodel_name='paket.perjalanan', 
        string='Travel Package')
    paket_peserta_line = fields.One2many(comodel_name='paket.peserta.line', 
        inverse_name='order_id', string='Manifest')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Customer',
        domain="[('is_customer','=',True)]")
    


    @api.onchange('paket_perjalanan_id')
    def _onchange_paket_perjalanan_id(self):
        for r in self:
            if r.paket_perjalanan_id:
                # removes all existing (previous) value from list
                lines=[(5,0,0)]
                line=self.paket_perjalanan_id.product_id
                vals={
                        'product_id':line.id,
                        'name':line.name,
                        'product_uom':1
                    }
                lines.append((0,0,vals))
                r.order_line=lines
                

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.model
    def create(self,vals):
        res=super(SaleOrderLine,self).create(vals)
        return res