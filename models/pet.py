# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Pet(models.Model):
    _name = "partners.pet"
    _description = "Mascotas de Clientes"

    name = fields.Char(string="Nombre", required=True)
    raza = fields.Selecction([('chihuahua', 'Chihuahua'), ('chitzu', 'Chitzu')], string="Raza")
    age = fields.Integer(string="Edad")
    weight = fields.Float(string="Peso")
    vaccinated = fields.Boolean(string="Vacunado")
    date = fields.Date(string="Fecha de Nacimiento")
    description = fields.Html(string="Descripcion")
    image = fields.Binary(string="Fotografia")

    @api.multi
    @api.depends("name", "age")
    def name_get(self):
        result = []
        for table in self:
            l_name = table.name + "-" + str(table.age)
            l_name += table.name
            result.append((table.id, l_name))
        return result
