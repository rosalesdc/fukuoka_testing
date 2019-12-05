# -*- coding:utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models

class PagosBancosPartner(models.Model):
    _inherit = 'account.payment'

    
    Banco_asociado = fields.Many2one('res.partner.bank',
                                     string="Banco Asociado",
                                     
                                     )

    
    @api.multi
    def get_email_partner(self):
        for record in self:
            if record.partner_id.email:
                print("Hay correo")
                correo = record.partner_id.email.split(",")
                if len(correo)>0:
                    return correo[0]
                else:
                    return ''
    
#    @api.onchange('partner_id')
#    def _onchange_partner(self):
#        print("HELLO")
#        self.Banco_asociado = self.partner_id.Banco_asociado