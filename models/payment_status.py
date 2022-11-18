from odoo import models, fields, api


class PaymentStatus(models.Model):
    _name = 'payment.status'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Payment Status'

    product_id = fields.Many2one("venue.list", string="Product ID")

    active = fields.Boolean(string="Active", default=True)