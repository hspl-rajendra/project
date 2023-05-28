from odoo import api, fields, models


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = "Appointment Cancellation Wizard"

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
    reason = fields.Text(string="Reason")
    cancel_appointment_time = fields.Datetime(string="Cancel Appointment Time", default=fields.Datetime.now)




    def action_cancel(self):
        self.appointment_id.reason = self.reason if self.reason else ""
        self.appointment_id.state = 'cancel'



































































































































