from odoo import models, fields, api


class VenueBookingTeam(models.Model):
    _name = 'venue.booking.team'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Venue Booking Team'

    name = fields.Char(string="Team Name")
    team_list = fields.Many2many("employee.information", string="Team List")

    active = fields.Boolean(string="Active", default=True)