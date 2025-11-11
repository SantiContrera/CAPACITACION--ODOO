from odoo import models, fields

class libraryWizardUpdate(models.TransientModel):
    _name = 'library.wizard.update'
    _description = 'Wizard para actualizar '

    book_copy_id = fields.Many2one('library.ejemplar', string='Ejemplares en stock')
    new_status = fields.Selection([
        ('stant', 'Disponible'),
        ('alquilado', 'Ocupado'),
        ('comprado', 'Comprado')
    ], string='Nuevo Estado', required=True)
    contacto_id = fields.Many2one('res.partner', string='Nuevo propietario')
    devolver = fields.Date('Fecha', default=fields.Date.today)

    def action_change_status(self):
        self.ensure_one()

        ejemplar = self.book_copy_id
        if not ejemplar:
            return {'type': 'ir.actions.act_window_close'}
        
        ejemplar.status = self.new_status

        if self.new_status == 'stant':
                self.book_copy_id.propietario_id = False
                self.book_copy_id.fecha = False
        elif self.new_status == 'alquilado':
                self.book_copy_id.propietario_id = self.contacto_id
                self.book_copy_id.fecha = self.devolver
        elif self.new_status == 'comprado':
                self.book_copy_id.propietario_id = self.contacto_id
                self.book_copy_id.fecha = False

        return {'type': 'ir.actions.act_window_close'}

