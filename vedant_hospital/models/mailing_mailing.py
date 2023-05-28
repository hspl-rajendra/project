from odoo import api, fields, models


class MailingMailing(models.Model):
    _name = 'mailing.mailing'
    _inherit = ['mailing.mailing']

    test=fields.Char(string="MailingMaling")



