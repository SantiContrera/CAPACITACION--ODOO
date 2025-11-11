from odoo import models, fields

class LibraryBookcategories(models.Model):
    _name = 'library.book.categories'
    _description = 'Categoria de libro'

    name = fields.Char(string='Nombre de la categoría', required=True)
    description = fields.Text(string = 'Descripcion')
