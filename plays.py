# -*- coding: utf-8 -*-
from odoo import models,fields

class plays(models.Model):
    _name = 'helloworld.plays'

    team1_id = fields.Many2one('helloworld.teams',string='Team')
    team2_id = fields.Many2one('helloworld.teams',string='Team')
    estadio_id = fields.Many2one('helloworld.places',string='Team')
    arbitro_id = fields.Many2one('helloworld.referees',string='Team')

    _order = 'team_id, name'
