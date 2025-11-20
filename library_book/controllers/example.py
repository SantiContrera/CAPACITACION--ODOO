from odoo import http
from odoo.http import request

class EjemplarControlador(http.Controller):
    @http.route('/library_book/informacion_ejemplares', auth='public', type='json')
    def ObtenerEjemplares(self):
        """Dato de ejemplar:"""
        aux = request.env['library.ejemplar'].search([])
        lenn = []
        for ejemplar in aux:
            lenn.append({
                #ID del ejemplar.
                'ID': ejemplar.id,
                #Código del ejemplar.
                'Codigo': ejemplar.ejemplar_id,
                #Nombre del ejemplar.
                'Nombre': ejemplar.titulo_id,
                #Fecha de devolución (si aplica).
                'Fecha de devolucion': ejemplar.fecha,
            })
        return lenn

    @http.route('/library_book/informacion_ejemplares/<int:ejemplar_id>', auth='user', type='json')
    def Ejemplar(self, ejemplar_id):
        aux = request.env['library.ejemplar'].browse(ejemplar_id)

        #si no existe el buscadp
        if not aux.exist():
            return {'error: ID no encontrado'}
        
        #traer plantilla
        template = request.env.ref('library_book_model.plantilla_ejemplar')

        # Enviar email
        template.send_ejemplar_mail(aux.id, force_send=True)

        return {
            #Nombre del ejemplar.
            'ejemplar': aux.ejemplar_id,
            #Quien lo alquilo/compro.
            'Propietario':aux.propietario_id,
            #Valor del ejemplar
            'precio':aux.precio,
        }
