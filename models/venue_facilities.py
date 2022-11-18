from odoo import models, fields, api

class VenueFacilities(models.Model):
    _name = 'venue.facilities'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Venue Facilities'

    food = fields.Char(string="Food Items")
    stage = fields.Char(string="Stage Qty")
    chair = fields.Char(string="Chair Qty")
    table = fields.Char(string="Table Qty")

    active = fields.Boolean(string="Active", default=True)