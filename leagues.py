# -*- coding: utf-8 -*-
from odoo import models,fields

class leagues(models.Model):
    _name = 'helloworld.leagues'

    #team_id = fields.Many2one('helloworld.teams',string='Team')
    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')
    city = fields.Char(string='Ciudad')
    state = fields.Char(string='Estado')
    team_id = fields.One2many('helloworld.teams', 'league_id', string='Team')
    places_id = fields.One2many('helloworld.places', 'league_id', string='Place')
    referee_id = fields.One2many('helloworld.referees', 'league_id', string='Referee')
    #numero = fields.Integer(string='Numero de playera')
    #posicion = fields.Selection( [('ban', 'Bandera'), ('cen', 'Central')], string = 'Tipo de arbitro' )

    _order = 'name'