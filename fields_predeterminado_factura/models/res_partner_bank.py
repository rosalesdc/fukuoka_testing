# -*- coding:utf-8 -*-

from odoo import fields
from odoo import models
from odoo import api

class BancosPartnerMods(models.Model):
	_inherit='res.partner.bank'

	x_clabe= fields.Char(string ='CLABE',size=18)
	