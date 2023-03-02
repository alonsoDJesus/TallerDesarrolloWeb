# -*- coding: utf-8 -*-
from odoo import models,fields

class players(models.Model):
    _name = 'helloworld.players'

    team_id = fields.Many2one('helloworld.teams',string='Team')
    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')
    numero = fields.Integer(string='Numero de playera')
    posicion = fields.Selection( [('del', 'Delantero'), ('def','Defensa'), ('port','Portero'), ('car','Carrilero'), ('cen', 'Central')], string = 'Número de la playera' )

    _order = 'team_id, name'
