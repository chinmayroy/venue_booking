from odoo import http
from odoo.http import request


class VenueBooking(http.Controller):
    @http.route('/booking', auth='user', website=True)
    def booking(self, **kw):
        booking_list = request.env['venue.booked.list'].sudo().search([])
        venue_list = request.env['venue.list'].sudo().search([])
        slot_list = request.env['venue.slot.list'].sudo().search([])
        values = {
            'booking_list': booking_list,
            'venue_list': venue_list,
            'slot_list': slot_list,
        }
        return request.render("venue_booking.booking_template_view", values)

    @http.route('/thank_you_message', auth='user', website=True)
    def thankyou(self, **kw):
        new_booking = request.env['venue.booked.list'].sudo().create(kw)
        values = {
            'new_booking': new_booking,
        }
        return request.render("venue_booking.successful_message", values)