/** @odoo-module **/

import { FormController } from '@web/views/form/form_controller';
import { Dialog } from '@web/core/dialog/dialog';

const CustomFormController = FormController.extend({
    async _validateAndSave() {
        const invalidFields = this.model.getInvalidFields(this.handle);
        if (invalidFields.length > 0) {

            const fieldsList = invalidFields.map(field => `<li>${field}</li>`).join("");
            const message = `
                <p>Les champs suivants sont invalides :</p>
                <ul>${fieldsList}</ul>
            `;
            Dialog.confirm(this, message, {
                title: "Validation des champs",
                confirmLabel: "Ok",
            });
            return false;
        }
        return this._super(...arguments);
    },
});

FormController.include(CustomFormController);
