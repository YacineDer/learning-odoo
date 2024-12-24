from odoo import models, fields

class Admission(models.Model):
    _name = 'clinique.admission'
    _description = 'Admission'

    patient_id = fields.Many2one('clinique.patient', string="Patient", required=True)
    medecin_id = fields.Many2one('clinique.medecin', string="Médecin", required=True)
    service_id = fields.Many2one('clinique.service', string="Service", required=True)
    admission_date = fields.Date(string="Date d'admission", default=fields.Date.today)
    status = fields.Selection([
        ('admitted', 'Admis'),
        ('discharged', 'Sorti')
    ], string="Statut", default='admitted')
