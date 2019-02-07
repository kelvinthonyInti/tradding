# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    pets = fields.Many2many(comodel_name="partners.pet", string="Mascotas")
