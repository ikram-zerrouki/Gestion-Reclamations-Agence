from odoo import models, fields

class GestionnaireReclamation(models.Model):
    _name = 'gestionnaire'
    _description = 'Gestionnaire de Réclamation'

    name = fields.Char(string='Nom', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Téléphone')
    role = fields.Selection([
        ('manager', 'Responsable'),
        ('agent', 'Agent de traitement'),
    ], string='Rôle', default='agent')
    active = fields.Boolean(string='Actif', default=True)
