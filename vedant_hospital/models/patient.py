# -*- coding: utf-8 -*-

from odoo import api, fields, models,_
from datetime import date
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
import xlwt
import base64
from io import BytesIO
from odoo import SUPERUSER_ID


class CustomExcel(models.TransientModel):
    _name = "custom.excel.class"
    _rec_name = "datas_fname"

    file_name = fields.Binary(string="Report")
    datas_fname = fields.Char(string="Filename")





class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread']
    _description = "Hospital Patient"
    _rec_name = "name"

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    name =fields.Char(string="Name", tracking=True,  required=True)
    date_of_birth=fields.Date(string="Date of Birth")
    ref = fields.Char(string="Reference")
    age =fields.Integer(string="Age",compute='_compute_age',tracking=True)
    gender=fields.Selection([('male','Male'),('female','female')],string="Gender",tracking=True,)
    active=fields.Boolean(string="Active",default=True)
    appointment_id= fields.Many2one('hospital.appointment', string="Appointments")
    image=fields.Image(string='Image')
    tag_ids=fields.Many2many('patient.tag',string="Tags")
    marital_status = fields.Selection([('married','Married'),('single','Single')],string="Marital status" ,tracking=True)
    phone=fields.Char(string="Phone")
    email=fields.Char(string="Email",copy=False)
    sequence=fields.Integer(string='Sequence' )



    @api.model_create_multi
    def create(self,vals):
        rtn= super(HospitalPatient,self).create(vals)

        return rtn


    @api.model_create_multi
    def create(self,vals):

        vals['ref']= self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient,self).create(vals)

    def name_get(self):
        result = []
        for rec in self:
            name = f'{rec.ref} - {rec.name}'
            result.append((rec.id,name))
            return result

    def write(self,values):
        if not self.ref:
            values['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient,self).write(values)

    def print_exel(self):
        filename = self.name
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet1 = workbook.add_sheet('staff',cell_overwrite_ok=True)
        format1 = xlwt.easyxf('align:horiz center;font:color black,bold True;borders:top_color black,bottom_color black,right_color black,left_color black,left thin,right thin,top thin,bottom thin;pattern:pattern solid, fore_color aqua')

        sheet1.col(0).width = 7000
        sheet1.write(0,0,self.name,format1)
        # sheet1.write(0, 1,"Email", format1)
        # sheet1.write(0, 2,"Moblie", format1)
        # sheet1.write(0, 3,"Age", format1)
        # sheet1.write(0, 4, self.ref, format1)
        # sheet1.write(0, 5, self.ref, format1)



        stream=BytesIO()
        workbook.save(stream)
        out = base64.encodebytes(stream.getvalue())

        excel_id = self.env['custom.excel.class'].create({'datas_fname':filename,
                                                          'file_name':out})


        return{
            'res.id': excel_id.id,
            'view_mode':"form",
            'type':'ir.actions.act_window',
            'view_type':"form",
            'res_model':'custom.excel.class',
            'view_id': False,
            'name':'Appointment Report'
        }


    # @api.depends('date_of_birth')
    # def _compute_age(self):
    #     # print("self.........",self)
    #     for rec in self:
    #         today = date.today()
    #         # print("date.today()",date.today())
    #         if rec.date_of_birth:
    #             # print("rec",rec,rec.name,rec.date_of_birth.year)
    #             # print("age", rec, rec.name, rec.date_of_birth.year)
    #             rec.age = today.year - rec.date_of_birth.year
    #         else:
    #             rec.age=0

    @api.depends('date_of_birth')
    def _compute_age(self):
        self.age = False
        for rec in self:
            rec.age = relativedelta(date.today(),rec.date_of_birth).years

    #
    # @api.depends('age')
    # def _inverse__compute_age(self):
    #     return





    def action_view_appointments(self):
        return {
            'name': _('Appointments'),
            'res_model': 'hospital.appointment',
            'view_mode': 'list,form,calendar,activity',
            'context': {'default_patient_id':self.id},
            'domain':[('patient_id','=',self.id)],
            'target': 'current',
            'type': 'ir.actions.act_window',
        }

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            patients = self.env['hospital.patient'].search([('name','=',rec.name),('id','!=',rec.id)])
            if patients:
                raise ValidationError(_("Name %s already Exists" % rec.name))

    @api.constrains('age')
    def check_age(self):
        for rec in self:
            if rec.age == 0:
                raise ValidationError(_("Age cannot be Zero"))

    def name_get(self):
        patient_list = []
        # self.env.context.get()
        for rec in self:
            name = rec.ref+''+rec.name
            patient_list.append((rec.id,name))
        return [(rec.id,"%s:%s "%(rec.ref,rec.name))for rec in self]
    #
    # @api.model
    # def create(self,vals):
    #     if vals.get("squ_num",_('New'))==_('New'):
    #         vals['squ.num'] = self.env["ir.sequence"].next_by_code('hospital.patient') or _('New')
    #     res = super(HospitalPatient, self).create(vals)
    #     return res


#when use odoo shell print for print output we must write command self.env.cr.commit()
