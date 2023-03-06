# -*- coding: utf-8 -*-
from odoo import models,fields

class places(models.Model):
    _name = 'helloworld.places'

    #team_id = fields.Many2one('helloworld.teams',string='Team')
    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')
    capacity = fields.Integer(string='Capacidad Máxima')
    league_id = fields.Many2one('helloworld.leagues', string='League')
    #numero = fields.Integer(string='Numero de playera')
    #posicion = fields.Selection( [('ban', 'Bandera'), ('cen', 'Central')], string = 'Tipo de arbitro' )

    _order = 'name'