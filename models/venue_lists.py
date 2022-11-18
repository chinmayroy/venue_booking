from odoo import models, fields, api, _


class VenueList(models.Model):
    _name = 'venue.list'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Venue List'

    name = fields.Char(string="Venue Name")
    product_id = fields.Char(string='Product ID', required=True, readonly=True, default=lambda self: _('New'), copy=False)
    team_name = fields.Many2one("venue.booking.team", string="Team Name")
    facilities = fields.Many2many("venue.facilities", string="Facilities")

    active = fields.Boolean(string="Active", default=True)

    @api.model
    def create(self, vals):
        if vals.get('product_id', _('New')) == _('New'):
            vals['product_id'] = self.env['ir.sequence'].next_by_code('venue.list') or _('New')
        res = super(VenueList, self).create(vals)
        return res