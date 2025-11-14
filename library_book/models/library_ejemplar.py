from odoo import models, fields, api

class LibraryEjemplar(models.Model):
    _name = 'library.ejemplar'
    _description = 'ejemplares'

    titulo_id = fields.Many2one('library.book.model', string='Titulo')
    book_id = fields.Many2one('library.book.model', string='ID DE EJEMPLAR')
    status = fields.Selection([
        ("stant",'Disponible'),
        ("alquilado",'Alquilado'),
        ("comprado", 'Comprado')
    ], default='stant', string='Estado')
    propietario_id = fields.Many2one('res.partner', string='Propietario')
    fecha = fields.Date('Fecha', default=fields.Date.today)
    email = fields.Char(string="Correo")
    description = fields.Text(string = 'Descripcion')
    user_id = fields.One2many('library.book.model', 'partner_id', string='Responsable')
    ejemplar_id = fields.Char(string='Nombre Ejemplar', compute='ejemplar_calc', store=True)

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

    @api.depends('titulo_id')
    def ejemplar_calc(self):
        for record in self:
            if record.titulo_id:
                ejemplares = self.search([('titulo_id', '=', record.titulo_id.id)], order='id')
                cantidad = ejemplares.ids.index(record.id) + 1 if record.id in ejemplares.ids else 1
                record.ejemplar_id = f"{record.titulo_id.tittle or 'Libro'}, {numero}"
            else:
                record.ejemplar_id = f"Ejemplar {record.id}"

