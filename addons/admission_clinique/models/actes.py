from odoo import models, fields

class Actes(models.Model):
    _name = 'clinique.actes'
    _description = 'Actes'

    name = fields.Char(string="Nom de l'acte", required=True)
    description = fields.Text(string="Description")
    service_ids = fields.Many2many('clinique.service', string="Services")
