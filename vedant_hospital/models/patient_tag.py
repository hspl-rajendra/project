from odoo import api, fields, models


class PatientTag(models.Model):
    _name = "patient.tag"

    _description = "Patient Tag"

    name=fields.Char(string='Name',required=True)
    color = fields.Integer(string="Color")
    active=fields.Boolean(string='Active',default=True)
    # color2 =fields.Char(string="Color 2")
