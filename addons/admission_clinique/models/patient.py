from odoo import models, fields, api

class Patient(models.Model):
    _name = 'clinique.patient'
    _description = 'Patient'

    name = fields.Char(string="Prénom", required=True)
    family_name = fields.Char(string="Nom de famille", required=True)
    birth_date = fields.Date(string="Date de naissance")
    gender = fields.Selection([
        ('male', 'Homme'),
        ('female', 'Femme'),
        ('other', 'Autre')
    ], string="Sexe")
    spouse_name = fields.Char(string="Nom du conjoint")
    age = fields.Integer(string="Âge", compute='_compute_age', store=True)

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                record.age = (fields.Date.today() - record.birth_date).days // 365
            else:
                record.age = 0
