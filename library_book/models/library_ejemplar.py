from odoo import models, fields

class LibraryEjemplar(models.Model):
    _name = 'library.ejemplar'
    _description = 'ejemplares'

   #titulo_id = fields.Many2one("library_book.model")
    book_id = fields.Many2one('library.book.model', string='Ejemplareses')
    status = fields.Selection([
        ("stant",'Disponible'),
        ("alquilado",'Alquilado'),
        ("comprado", 'Comprado')
    ], default='stant', string='Estado')
    propietario_id = fields.Many2one('res.partner', string='Propietario')
    fecha = fields.Date('Fecha', default=fields.Date.today)
    email = fields.Char(string="Correo")
    description = fields.Text(string = 'Descripcion')

    def actio(self):
        if self.status == 'stant':
            self.propietario_id = False
            self.fecha = False
        elif self.status == 'alquilado':
            self.propietario_id = self.propietario_id
            self.fecha = self.fecha
        elif self.status == 'comprado':
            self.propietario_id = self.propietario_id
            self.fecha = False


