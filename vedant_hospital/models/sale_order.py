from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    test = fields.Char(string='SaleOrder')
    patient_ids = fields.Many2one('hospital.patient', string="Patient")



    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        print(self.partner_id.name)


    #
    # def _get_sale_order_name(self, partner_id, context=None):
    #     partner = self.env['res.partner'].browse(partner_id)
    #     partner_name = partner.name
    #     if context and 'zip_code' in context:
    #         partner_name += ' - ' + context['zip_code']
    #     return partner_name


