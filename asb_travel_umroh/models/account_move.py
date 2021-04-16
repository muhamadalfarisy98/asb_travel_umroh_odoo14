from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def button_cetak_pdf(self):
        if self._context.get('customer_invoice_report'):
            return self.env.ref('asb_travel_umroh.report_account_move').report_action(self.id)

    def get_payment_ids(self):
        payment_ids=self.env['account.payment'].sudo().search(
            [
                ('ref','=',self.name)
            ]
        )
        return payment_ids