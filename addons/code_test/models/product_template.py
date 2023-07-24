from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    margin = fields.Float(compute='compute_margin', readonly=False, string='Margin %')

    @api.depends('list_price', 'standard_price')
    def compute_margin(self):
        for record in self:
            record.margin = (record.list_price - record.standard_price) / record.list_price * 100

    @api.onchange('margin')
    def onchange_margin(self):
        """
            TODO: If you change margin, the list price should be changes to correct values,
            Like its done in compute_margin function but other way around.
            Check how margin is calculated and make neccessary changes so result is correct
        """
        self.list_price = self.standard_price + self.margin
