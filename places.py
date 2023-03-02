# -*- coding: utf-8 -*-
from odoo import models,fields

class places(models.Model):
    _name = 'helloworld.places'

    #team_id = fields.Many2one('helloworld.teams',string='Team')
    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')
    city = fields.Char(string='Ciudad')
    state = fields.Char(string='Estado')
    capacity = fields.Integer(string='Capacidad Máxima')
    #numero = fields.Integer(string='Numero de playera')
    #posicion = fields.Selection( [('ban', 'Bandera'), ('cen', 'Central')], string = 'Tipo de arbitro' )

    _order = 'name'