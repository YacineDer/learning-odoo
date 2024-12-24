from odoo import models, fields

class Service(models.Model):
    _name = 'clinique.service'
    _description = 'Service'

    name = fields.Char(string="Nom du service", required=True)
    description = fields.Text(string="Description")
    medecin_ids = fields.Many2many('clinique.medecin', string="Médecins")
    actes_ids = fields.Many2many('clinique.actes', string="Actes")
