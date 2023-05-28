from odoo import api, fields, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

    is_a_member = fields.Boolean(string="Is A Member")

    membership_level_id = fields.Many2one('membership.level', string="MembershipID")

