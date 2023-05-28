from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import timedelta


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_a_member = fields.Boolean(string="Is A Member", related='partner_id.is_a_member')



    @api.constrains('date_order')
    def _date_order_date(self):
        for rec in self:
            if rec.date_order.date() < fields.Date.today():
                raise ValidationError("You can't add previous Date")

    @api.constrains('validity_date')
    def check_expiration_date(self):
        for rec in self:
            test = fields.Date.today()
            print(test)
            min_expiration_date = rec.validity_date + timedelta(days=5)
            print(min_expiration_date)
            if min_expiration_date <= test:
                raise ValidationError("Expiration Date should be at least 5 a Quotation Date.")
