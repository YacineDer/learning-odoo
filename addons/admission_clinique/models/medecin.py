from odoo import models, fields

class Medecin(models.Model):
    _name = 'clinique.medecin'
    _description = 'Médecin'

    name = fields.Char(string="Nom", required=True)
    specialty = fields.Char(string="Spécialité")
    service_ids = fields.Many2many('clinique.service', string="Services")
