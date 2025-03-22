from odoo import models, fields, api

class Deplacement(models.Model):
    _name = 'deplacement'
    _description = 'Déplacement lié à un traitement'

    name = fields.Char(string="Nom du déplacement", required=True)
    traitement_id = fields.Many2one(
        'traitement',
        string="Traitement associé",
        required=True,
        help="Traitement lié à ce déplacement"
    )
    date_deplacement = fields.Date(string="Date du déplacement", required=True)
    equipe_id = fields.Many2one('equipe', string="Équipe responsable", help="Équipe effectuant ce déplacement")
    actions_realisees = fields.Text(string="Actions réalisées", help="Liste des actions effectuées lors du déplacement")
    remarques = fields.Text(string="Remarques", help="Commentaires ou observations liés au déplacement")
    

    @api.model
    def unlink(self):
        for record in self:
            if record.related_model_id:
                raise UserError("Cannot delete this record because it is linked to another model.")
        return super(Deplacement, self).unlink()
