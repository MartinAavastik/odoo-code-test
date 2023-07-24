from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # TODO: Add new field called "Line Comment", where you can enter text and add it to SaleOrder form view
