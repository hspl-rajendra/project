import io
import json

try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter

from odoo import fields, models


class VendorReportWizard(models.TransientModel):
    _name = 'vendor.report.wizard'
    _description = 'Vendor Report Wizard'

    vendor_ids = fields.Many2many('res.partner', string='Vendors')

    def vendor_report_print(self):
        purchase_obj = self.env['purchase.order']
        for vender_id in self.vendor_ids:
            purchase_ids = purchase_obj.search([('partner_id', '=', vender_id.id)])

        headers = [
            "PO #",
            "Date",
            "Vendor Name",
            "Status",
            "Total Amount"
        ]
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet('Membership')
        bold = workbook.add_format({"bold": True})
        date_format = workbook.add_format(
            {"text_wrap": True, "num_format": "dd-mm-yyyy"}
        )
        row = 0
        column = 0
        for header in headers:
            sheet.set_column(row, column, 19)
            sheet.write(row, column, header, bold)
            column = column + 1

        row = 1
        i = 0
        for rec in purchase_ids:
            column = 0
            sheet.write(row, column, rec.name or "")
            column = column + 1
            sheet.write(row, column, rec.date_order, date_format)
            column = column + 1
            sheet.write(row, column, rec.partner_id.name or "")
            column = column + 1
            sheet.write(row, column, rec.state or "")
            column = column + 1
            sheet.write(row, column, rec.amount_total or "")
            column = column + 1
            row = row + 1
            i = i + 1
