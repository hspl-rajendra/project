from odoo import api, fields, models, _


class AppointmentReportWizard(models.TransientModel):
    _name = 'appointment.report.wizard'
    _description = 'Appointment Report Wizard'

    patient_id = fields.Many2one('hospital.patient', string="Appointment")
    date_from = fields.Date(string='From Date')
    date_to = fields.Date(string='To Date')

    def action_print_report(self):
        domain = []
        patient_id = self.patient_id
        if patient_id:
            domain += [('patient_id', '=', patient_id.id)]
        date_from = self.date_from
        if date_from:
            domain += [('appointment_time', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('appointment_time', '<=', date_to)]
        appointments = self.env['hospital.appointment'].search_read(domain)
        print('----------', appointments)
        data = {
            'from_data': self.read()[0],
            'appointments': appointments
        }
        return self.env.ref('vedant_hospital.action_report_appointment').report_action(self, data=data)
