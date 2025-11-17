from odoo import models, fields, api

class LibrosModel(models.Model):
    _name = 'library.book.model'
    _description = 'GUardar libros'

    partner_id = fields.Many2one('res.partner', string='Usuario responsable', ondelete='set null')
    category_id = fields.Many2one('library.book.categories', string='Categoria de libro')
    copies_id = fields.One2many('library.ejemplar', 'titulo_id', string='titulo')
    prop_id = fields.One2many('library.ejemplar', 'propietario_id', string='Actual propietario')
    estado_id = fields.Many2one('library.ejemplar', string='Estado')

    tittle = fields.Char(string='Titulo', required=True)
    price = fields.Monetary(string='Precio', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Moneda')

    author = fields.Char(string='Autor', required=True)
    date = fields.Date(string='Fecha de lanzamiento', required=True)
    summary = fields.Char(string='Resumen')
    total_pages = fields.Integer(string='Total de paginas', default=0)
    act = fields.Boolean(string="El autor sigue escribiendo hoy en dia", default=True)

    



