# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalLab(models.Model):
    _name = "hospital.lab"
    _discripation='Hospital Lab'
    _inherit = ['mail.thread']
    _inherits = {'res.users': 'user_id'}

    # _log_access= False

    name = fields.Char( string='Name')

    user_id = fields.Many2one('res.users',string="Responsible")


class AccountBankStatementLine(models.Model):
    _name = "lab.employee"
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one("res.partner", string="Lab Employee")



class HSPL(models.Model):
    _name = "hspl.employee"
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one("res.partner", string="HSPL")