# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = "patient_id"

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    gender = fields.Selection([('male', 'Male'), ('female', 'female')], related='patient_id.gender')
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    ref = fields.Char(string="Reference", help="Reference of the patient from patient record")
    prescripation = fields.Html(string='Prescripation')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")  # used to order
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In_consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default='draft', string="Status", required=True)
    doctor_id = fields.Many2one('res.users', string='Doctor')
    pharmacy_lines_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', 'Pharmacy Lines')
    hide_sales_price = fields.Boolean(string="Hide_Sales_Prices")

    # avatar_images_1920 = fields.Image("Avatar")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print("Button click!!!!!!!!!!!!!!!!!!!!!!!")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': "Click Sucessfull",
                'type': 'rainbow_man',
            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = "done"

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"

    def action_draft(self):
        for rec in self:
            rec.state = "draft"


class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _descripation = "Appointment Pharmacy Lines"

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(string='Price', related='product_id.list_price')
    qty = fields.Integer(string='Quantity', default='1')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    avatar_images_1920=fields.Image(string='avatar_images_1920')

