from odoo import models, fields, api

class Reclamation(models.Model):
    _name = 'reclamation'
    _description = 'Gestion des Réclamations'

    # Identifiant unique pour chaque réclamation (généré automatiquement)
    name = fields.Char(string="Réclamation ID", required=True)
    
    # Informations de base
    date = fields.Date(string="Date de la réclamation", default=fields.Date.today, required=True)
    objet = fields.Char(string="Objet", required=True)
    description = fields.Text(string="Description", required=True)
    reclamant_name = fields.Char(string="Nom du réclamant", required=True)
    reclamant_phone = fields.Char(string="Téléphone", required=True)
    reclamant_email = fields.Char(string="Email", required=False)
    reclamant_address = fields.Text(string="Adresse")
    reclamant_commune = fields.Char(string="Commune")
    reclamant_type = fields.Selection(
        [('citoyen', 'Citoyen'), ('entreprise', 'Entreprise'), ('cellule_veille', 'Cellule de Veille')],
        string="Type de réclamant",
        required=True
    )
    
     
    entreprise_phone = fields.Char(string="Téléphone de l'entreprise")
    entreprise_address = fields.Text(string="Adresse de l'entreprise")
    
    
     
    
    source_reclamation = fields.Selection([
    ('telephone', 'Par téléphone'),
    ('visite_agence', 'Lors d\'une visite en agence'),
    ], string="Mode de réception", required=True)

    documents = fields.Binary(string="Documents justificatifs")
    document_name = fields.Char(string="Nom du document")



    # Informations sur la gestion interne 
    agence_id = fields.Many2one(
    'res.company',
    string="Agence",
    required=True,
    default=lambda self: self.env.company
)

    urgence = fields.Selection([('faible', 'Faible'), ('moyenne', 'Moyenne'), ('haute', 'Haute')], string='Urgence')
    type_reclamation = fields.Selection(
        [('technique', 'Technique'), ('commercial', 'Commercial')],
        string="Type de réclamation",
        required=True
    )
    etat = fields.Selection(
        [('nouveau', 'Nouveau'), ('en_cours', 'En cours'), ('traite', 'Traité'), ('cloture', 'Clôturé')],
        string="État de la réclamation",
        default='nouveau',
        required=True
    )

    notes_internes = fields.Text(string="Notes internes")
    
    
    # ------------------------- cellule de veille 
    
    details_media = fields.Text(string="Détails du média")
    source_media = fields.Selection([
    ('journal', 'Journal'),
    ('site_web', 'Site Web'),
    ('television', 'Télévision'),
    ('autre', 'Autre')
], string="Source de la réclamation", required=True)
    
   
    
    
    @api.onchange('reclamant_type')
    def _onchange_reclamant_type(self):
        if self.reclamant_type != 'entreprise':
            self.entreprise_phone = False
            self.entreprise_address = False

