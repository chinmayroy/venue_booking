from odoo import http
from odoo.http import request
import datetime


class VenueBooking(http.Controller):
    @http.route('/booking', auth='user', website=True)
    def booking(self):
        booking_list = request.env['venue.booked.list'].sudo().search([])
        venue_list = request.env['venue.list'].sudo().search([])
        slot_list = request.env['venue.slot.list'].sudo().search([])
        values = {
            'booking_list': booking_list,
            'venue_list': venue_list,
            'slot_list': slot_list,
        }
        return request.render("venue_booking.booking_template_view", values)

    @http.route('/booking/thank_you_message', auth='user', website=True)
    def thankyou(self, **kw):
        new_booking = request.env['venue.booked.list'].sudo().create(kw)

        user = http.request.env.user.partner_id.id
        venue_id = new_booking.venue_name
        venue_list_id = request.env['venue.list'].sudo().search([('id', '=', venue_id.id)], limit=1)

        today = datetime.datetime.now()
        invoice = request.env['account.move'].sudo().create({
            'move_type': 'out_invoice',
            'date': '2017-01-01',
            'partner_id': user,
            'invoice_date': today.strftime('%Y-%m-%d'),
            'invoice_line_ids': [
                (0, None, {
                    'product_id': venue_list_id.product_id.id,
                    'quantity': 1,
                    'price_unit': 500,
                }),
            ]
        })
        invoice.action_post()
        new_booking.create_email_receive_information()
        values = {
            'new_booking': new_booking,
            'invoice': invoice,
        }
        return request.render("venue_booking.successful_message", values)
