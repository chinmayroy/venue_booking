from odoo import models, fields, api, _


class VenueList(models.Model):
    _name = 'venue.list'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Venue List'

    name = fields.Char(string="Venue Name")
    product_id = fields.Many2one('product.product', string='Product ID')
    team_name = fields.Many2one("venue.booking.team", string="Team Name")
    facilities = fields.Many2many("venue.facilities", string="Facilities")

    active = fields.Boolean(string="Active", default=True)