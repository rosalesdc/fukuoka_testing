# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models


class ContactoAddBancos(models.Model):
    _inherit = 'res.partner'

    banco_ids = fields.One2many(
        'res.partner.bancos',
        'partner_id',
        string="Cuentas de Banco",
    )
