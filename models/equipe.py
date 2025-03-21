from odoo import models, fields

class equipe(models.Model):
    _name = 'equipe'
    _description = 'Équipe de réclamation'

    name = fields.Char(string="Nom de l'équipe", required=True)
    type_equipe = fields.Selection([
        ('technique', 'Technique'),
        ('commerciale', 'Commerciale'),
    ], string="Type d'équipe", required=True)
    
    membres_ids = fields.Many2many('res.partner', string="Membres", help="Liste des membres de l'équipe")
    
    reclamation_id = fields.Many2one('reclamation', string="Réclamation liée", help="Réclamation associée à cette équipe")
