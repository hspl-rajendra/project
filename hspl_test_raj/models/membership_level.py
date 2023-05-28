from odoo import fields, api, models


class MembershipLevel(models.Model):
    _name = 'membership.level'
    _description = "Membership Level"
    _order = 'ranking'

    _sql_constraints = [
        ('ranking_unique', 'unique(ranking)',
         "Already exists?.")
    ]

    name = fields.Char(string="Name")
    ranking = fields.Integer(string='Ranking')
    display_name = fields.Char(string='Display Name')
    tag_ids = fields.Many2many('ranking.tag', string='Tags')

    color = fields.Char(string='Color', store=True, compute='_compute_color_display')

    def _compute_color_display(self):
        for rec in self:
            print(self.color)
