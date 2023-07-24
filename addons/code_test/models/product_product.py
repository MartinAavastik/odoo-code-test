from odoo import fields, models, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def get_related_product_ids(self):
        self.ensure_one()
        """
            TODO: Find related products and return list of ProductProduct ids

            Related products are products that have been purchased alongside the given product

            detail:
                order the results by popularity, where popularity is defined by the number of times a product has been purchased (not the quantity of the product in any given order)
                Limit the result to 5 related products if there are more

            Finds related products given a product identifier
            inputs: unique identifier of a product
            outputs: list of ProductProduct ids

            HINT: https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#sql-execution
        """
        related_product_ids = self.env['product.product']
        return related_product_ids.ids
