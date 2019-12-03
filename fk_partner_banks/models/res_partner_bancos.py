# -*- coding: utf-8 -*-
from odoo import api, fields, models


class BancosClientes(models.Model):
    _name = 'res.partner.bancos'

    name = fields.Many2one(
        'res.bank',
        string='Banco'
    )

    acc_number = fields.Char(
        string='Número de cuenta'
    )

    edi_clabe = fields.Char(
        string='CLABE'
    )

    partner_id=fields.Many2one(
        'res.partner',
        string='Contacto'
    )
