from odoo import models, fields, api

class LibraryEjemplar(models.Model):
    _name = 'library.ejemplar'
    _description = 'ejemplares'

    titulo_id = fields.Many2one('library.book.model', string='Titulo')
    titulo_name = fields.Char(related='titulo_id.tittle', store=True)
    #book_id = fields.Many2one('library.book.model', string='titulo')
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
    precio = fields.Monetary(string='Precio', currency_field='currency_id', related='titulo_id.price', readonly=True, store=True)
    currency_id = fields.Many2one(related='titulo_id.currency_id', readonly=True, store=True)

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
                ejemplares = self.search([('titulo_id', '=', record.titulo_id.id)], order='create_date')
                
                count = 0
                for e in ejemplares:
                    if e.id < record.id or not record.id:
                        count += 1
                #record.cant= count

                record.ejemplar_id = f"{record.titulo_id.tittle}, {count + 1}"
            else:
                record.ejemplar_id = "Ejemplar sin título"

    #def action_quotation_send(self):
    def send_ejemplar_mail(self):
        """Enviar correo usando la plantilla_ejemplar."""
        template = self.env.ref('library_book.plantilla_ejemplar')
        for ejemplar in self:
            template.send_mail(ejemplar.id, force_send=True)

   