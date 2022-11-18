from odoo import models, fields, api


class VenueSlotList(models.Model):
    _name = 'venue.slot.list'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Venue Slot List'

    name = fields.Char(string="Venue Slot")

    active = fields.Boolean(string="Active", default=True)