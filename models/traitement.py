from odoo import models, fields


class Traitement(models.Model):
    _name = 'traitement'
    _description = 'Traitement de la réclamation'

    name = fields.Char(string="Nom du traitement", required=True)
    reclamation_id = fields.Many2one('reclamation', string="Réclamation associée", required=True, help="Réclamation liée à ce traitement")
    equipe_id = fields.Many2one('equipe', string="Équipe assignée", help="Équipe responsable du traitement")
    date_debut = fields.Date(string="Date de début", required=True)
    date_fin = fields.Date(string="Date de fin prévue")
    date_cloture = fields.Date(string="Date de clôture réelle", help="Date réelle de fin du traitement")
    etat_traitement = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
        ('annule', 'Annulé')
    ], string="État du traitement", default='brouillon')

    notes_internes = fields.Text(string="Notes internes", help="Commentaires ou remarques internes sur le traitement")
    actions_requises = fields.Text(string="Actions requises", help="Liste des actions nécessaires pour résoudre la réclamation")

    pv_text = fields.Text(string="Contenu du PV", help="Procès-verbal du traitement")

    # Nouveau champ One2many pour gérer les déplacements
    deplacement_ids = fields.One2many(
        'deplacement',  # Nom du modèle lié
        'traitement_id',  # Nom du champ Many2one dans le modèle 'deplacement'
        string="Déplacements",
        help="Liste des déplacements associés à ce traitement"
    )
    

    #def action_generate_pv(self):
    #return self.env.ref('gestion_des_reclamations.report_treatment_pv').report_action(self)
    #def action_generate_pv(self):
    #return self.env.ref('almiyah_djazair.report_treatment_pv').report_action(self)
    #def action_generate_pv(self):
        # Appel direct du rapport à partir de la référence du rapport
    #    return self.env.ref('djazair.report_treatment_pv').report_action(self)

    # Fonction pour générer le PV
    #def action_generate_pv(self):
        # Appel de la méthode pour générer le rapport
     #   report = self.env.ref('AlMiyah-Djazair.report_treatment_pv_view')
      #  return report.report_action(self)
    
    #def action_generate_pv(self):
     #   return self.env.ref('AlMiyah-Djazair.action_report_traitement_pv').report_action(self)


   