from odoo import http
from odoo.http import request
import datetime


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

    @http.route('/booking/bill_pay', auth='user', website=True)
    def bill_pay(self):
        partner_id = request.env['res.users'].browse()
        currency_id = request.env['account.move'].browse()
        if not currency_id:
            currency_id = request.env.ref['base.USD'].id
        p_name = request.env['product.product'].browse()
        product_id = request.env['product.product'].browse()
        price_unit = request.env['product.product'].browse()
        tax_ids = request.env['product.product'].browse()
        today = datetime.datetime.now()
        return request.env['account.move'].create({
            'move_type': 'in_invoice',
            'date': '2017-01-01',
            'partner_id': partner_id,
            'invoice_date': today,
            'currency_id': currency_id,
            'invoice_line_ids': [
                (0, None, {
                    'name': p_name,
                    'product_id': product_id,
                    'quantity': 1,
                    'price_unit': price_unit,
                    'tax_ids': tax_ids,
                }),
            ]
        })
        # return request.render("venue_booking.booking_bill_pay", move)

    @http.route('/booking/thank_you_message', auth='user', website=True)
    def thankyou(self, **kw):
        new_booking = request.env['venue.booked.list'].sudo().create(kw)
        values = {
            'new_booking': new_booking,
        }
        return request.render("venue_booking.successful_message", values)
