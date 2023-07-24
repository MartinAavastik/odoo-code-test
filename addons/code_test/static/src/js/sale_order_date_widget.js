odoo.define('code_test.SaleOrderDateWidget', function (require) {
    "use strict";

    var basic_fields = require('web.basic_fields');
    var field_registry = require('web.field_registry');

    var SaleOrderDateWidget = basic_fields.FieldDateTime.extend({
        // TODO: Show date green if date is in the future, red if in past
    });

    field_registry.add('sale_order_date_widget', SaleOrderDateWidget);

    return SaleOrderDateWidget;
});
