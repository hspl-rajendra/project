# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models



class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread']
    _description = "Hospital Patient"
    _rec_name = "name"


    name =fields.Char(string="Name", tracking=True)
    date_of_birth=fields.Date(string="Date of Birth")
    ref = fields.Char(string="Reference")
    age =fields.Integer(string="Age",compute='_compute_age',tracking=True)
    gender=fields.Selection([('male','Male'),('female','female')],string="Gender",tracking=True,)
    active=fields.Boolean(string="Active",default=True)
    appointment_id= fields.Many2one('hospital.appointment', string="Appointments")
    image=fields.Image(string='Image')
    tag_ids=fields.Many2many('patient.tag',string="Tags")

    @api.depends('date_of_birth')
    def _compute_age(self):
        print("self.........",self)
        for rec in self:
            today = date.today()
            print("date.today()",date.today())
            if rec.date_of_birth:
                print("rec",rec,rec.name,rec.date_of_birth.year)
                print("age", rec, rec.name, rec.date_of_birth.year)
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age=0


