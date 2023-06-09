from odoo import api,fields,models



class HospitalOperation(models.Model):
    _name = "hospital.operation"
    _discripation='Hospital Operation'
    # _log_access= False

    doctor_id = fields.Many2one('res.users', string='Doctor')
    operation_name=fields.Char(string="OperationName")
    reference_record= fields.Reference(selection=[('hospital.patient','Patient'),
                                                  ('hospital.appointment','Appointment')] ,string='Record')

    @api.model
    def name_create(self, name):

        return self.create({'operation_name': name}).name_get()[0]

