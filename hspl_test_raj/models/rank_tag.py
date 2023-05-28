from odoo import api, fields, models

class RankingTag(models.Model):
    _name ='ranking.tag'
    _description = 'Ranking Tags'

    name = fields.Char('Name', required=True)
    color = fields.Text(string='color')
    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer(string='Sequence')