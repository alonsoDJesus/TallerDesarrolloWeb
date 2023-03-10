# -*- coding: utf-8 -*-
from odoo import models,fields


class coachs(models.Model):
    _name = 'helloworld.coachs'
    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')

    _order = 'name'


class teams(models.Model):
    _name = 'helloworld.teams'

    name = fields.Char(string='Nombre')
    coach_id = fields.Many2one('helloworld.coachs',string='Coach')
    photo = fields.Binary(string='Foto')
    player_ids = fields.One2many('helloworld.players', 'team_id' ,string='Team')
    league_id = fields.Many2one('helloworld.leagues', string='League')

    _order = 'name'
