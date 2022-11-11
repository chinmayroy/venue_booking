from odoo import models, fields, api


class VenueBookingList(models.Model):
    _name = 'venue.booking.list'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Venue Booking List'

    name = fields.Char(string="Customer Name")
    email = fields.Char(string="Email")
    contact = fields.Char(string="Contact Number")
    program = fields.Char(string="Program Name")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    details = fields.Text(string="More Details")

    def action_send_email(self):
        template = self.env.ref('venue_booking.venue_booking_email_template')
        for rec in self:
            template.send_mail(rec.id, force_send=True)