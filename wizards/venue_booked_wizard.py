from datetime import date
from odoo import models, fields, api, _


class VenueBookedListCheck(models.TransientModel):
    _name = "venue.booked.list.check"
    _description = "Venue Booked List Print"

    customer_name = fields.Many2one("venue.booked.list", string="Customer Name:")
    date_from = fields.Date(string="Date From:")
    date_to = fields.Date(string="Date To:")

    def action_print_venue_booked_list(self):
        datalist = []
        venue_booked_w = self.env['venue.booked.list'].sudo().search(
            [('create_date', '>=', self.date_from), ('create_date', '<=', self.date_to)])
        for v in venue_booked_w:
            values = {
                'name': v.name,
                'email': v.email,
                'phone': v.phone,
                'program': v.program,
                'venue_name': v.venue_name.name,
            }
            datalist.append(values)
        data = {
            'form_data': self.read()[0],
            'venue_booked_w': datalist
        }
        return self.env.ref('venue_booking.action_venue_booked_wizard_report_view').report_action(self, data=data)