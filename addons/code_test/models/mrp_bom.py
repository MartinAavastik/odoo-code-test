# TODO: Please refactor using the correct code formatting rules
# You should also check out odoo python style guide at https://www.odoo.com/documentation/14.0/developer/misc/other/guidelines.html#python
from odoo import fields
from odoo import models
from odoo import api
class add_weight(models.Model):
    _inherit = 'mrp.bom'
    weight = fields.Float("Weight", compute='calculate_weight', digits='Stock Weight', store=True)

    @api.depends('bom_line_ids.product_qty')
    def calculate_weight(self):
        for bom in self:        
            bom.weight = self.getBomWeight(bom)
    def getBomWeight(reccs, self):
        x = 0
        for y in reccs.bom_line_ids:
            x = x + y.product_id.weight * y.product_qty
        return x   