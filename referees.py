# -*- coding: utf-8 -*-
from odoo import models,fields

class referees(models.Model):
    _name = 'helloworld.referees'

    #team_id = fields.Many2one('helloworld.teams',string='Team')
    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')
    #numero = fields.Integer(string='Numero de playera')
    posicion = fields.Selection( [('ban', 'Bandera'), ('cen', 'Central')], string = 'Tipo de arbitro' )

    _order = 'name'