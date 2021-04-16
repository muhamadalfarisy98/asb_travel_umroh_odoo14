from odoo import api, fields, models


class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'

    def button_cetak_pdf(self):
        if self._context.get('stock_picking_report'):
            return self.env.ref('asb_travel_umroh.report_stock_picking').report_action(self.id)