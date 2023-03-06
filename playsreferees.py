# -*- coding: utf-8 -*-
from odoo import models,fields

class playsreferees(models.Model):
    _name = 'helloworld.playsreferees'

    play_id = fields.Many2one('helloworld.plays', string='League')
    referee_id = fields.Many2one('helloworld.referees',string='Team')

    _order = 'name'