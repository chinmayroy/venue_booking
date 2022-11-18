from odoo import models, fields, api


class VenueBookedList(models.Model):
    _name = 'venue.booked.list'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Venue Booking List'

    name = fields.Char(string="Customer Name")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone Number")
    program = fields.Char(string="Program Name")
    venue_name = fields.Many2one("venue.list", string="Venue")
    slot = fields.Many2one("venue.slot.list", string="Slot")
    details = fields.Text(string="More Details")

    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('requirement', 'Requirement'),
        ('approved', 'Approved')], default='draft', string="Status")

    _sql_constraints = [
        ('unique_date', 'unique(slot)',
         'This slot {} already booked by someone!\nPlease select another slot.'.format(slot))
    ]

    def action_requirement(self):
        self.state = 'requirement'

    def action_approved(self):
        self.state = 'approved'
        template = self.env.ref('venue_booking.venue_booking_email_template')
        for rec in self:
            template.send_mail(rec.id, force_send=True)
