from odoo import models, fields, api


class EmployeeInformation(models.Model):
    _name = 'employee.information'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Employee Information'

    name = fields.Char(string="Employee Name")
    designation = fields.Char(string="Designation")

    active = fields.Boolean(string="Active", default=True)