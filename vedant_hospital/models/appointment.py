# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

import xlwt
import base64
from io import BytesIO
from odoo import SUPERUSER_ID



class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = "ref"

    partner_id = fields.Many2one('res.partner', string='Customer')
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
    reason = fields.Text(string='Reason')
    progress = fields.Integer(string="Progress", compute='_compute_progress')
    operation = fields.Many2one('hospital.operation', string='Operation')
    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', "Currency", related='company_id.currency_id', required=True)
    product_ids = fields.Many2many("product.product", string="Products")
    # avatar_images_1920 = fields.Image("Avatar")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref




    def action_test(self):
        # url action
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': 'https://www.odoo.com'
        }


    def check_orm(self):
        # search_var = self.env['hospital.patient'].create({
        #     "name": "check sucess"
        # })
        # print("|||||||||||||||||||||||||||||||||||", search_var)
        for rec in self:
            print("ODOOOOOOOOO")
            output = self.env['hospital.appointment'].search([])
            print("hello odoo........", output.mapped('ref'))
            print("1hello oddo>>>>", output.sorted(lambda r: r.write_date))
            print("2hello oddo>>>>", output.filtered(lambda r: not r.hide_sales_price))


    def action_share_whatsapp(self):
        if not self.patient_id.phone:
            raise ValidationError(_("Missing Phone Number"))
        message = 'Hi %s' % self.patient_id.name
        whatsapp_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' % (self.patient_id.phone, message)
        print("whatsapp_api_urlwhatsapp_api_url", whatsapp_api_url)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': whatsapp_api_url

        }

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = "done"

        return {
            'effect': {
                'fadeout': 'slow',
                'message': "Done",
                'type': 'rainbow_man',
            }
        }

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"

    def submit(self):
        search_var_ids = self.env['sale.order'].search([('partner_id', '=', self.partner_id.id)])
        product_ids = search_var_ids.mapped('order_line').mapped('product_id')
        print(product_ids)
        self.product_ids = [(6, 0, product_ids.ids)]


    def action_draft(self):
        for rec in self:
            rec.state = "draft"


    @api.depends('state')
    def _compute_progress(self):
        for rec in self:
            if rec.state == 'draft':
                progress = 25
            elif rec.state == 'in_consultation':
                progress = 50
            elif rec.state == 'done':
                progress = 100
            else:
                progress = 0
            rec.progress = progress


class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _descripation = "Appointment Pharmacy Lines"

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(string='Price', related='product_id.list_price')
    qty = fields.Integer(string='Quantity', default='1')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    currency_id = fields.Many2one('res.currency', related='appointment_id.currency_id')
    avatar_images_1920 = fields.Image(string='avatar_images_1920')
    price_subtotal = fields.Monetary(string='Subtotal', compute='_compute_price_subtotal')

    @api.depends('price_unit', 'qty')
    def _compute_price_subtotal(self):
        for rec in self:
            rec.price_subtotal = rec.price_unit * rec.qty

    @api.model
    @api.model
    def create(self, values):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..")
        # # Add code here
        # return super(ClassName, self).create(values)
