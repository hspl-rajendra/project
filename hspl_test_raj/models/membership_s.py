# -*- coding: utf-8 -*-
from odoo import api, fields, models


class MembershipS(models.Model):
    _name = "membership.s"
    _discripation='membership level'
    _inherit = ['mail.thread']
    _inherits = {'res.users': 'user_id'}

    # _log_access= False

    name = fields.Char( string='Name')

    user_id = fields.Many2one('res.users',string="Responsible")

