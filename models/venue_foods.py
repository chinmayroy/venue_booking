from odoo import models, fields, api

class VenueFoods(models.Model):
    _name = 'venue.foods'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Venue Facilities'

    food_name = fields.Char(string="Food Name")
    packet_qty = fields.Integer(string="Packet Qty")

    active = fields.Boolean(string="Active", default=True)