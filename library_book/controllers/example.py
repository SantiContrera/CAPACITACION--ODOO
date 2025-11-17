from odoo import http
from odoo.http import request

class EjemplarControlador(http.Controller):
    @http.route('/library_book/informacion_ejemplares', auth='public', type='json')
    def ObtenerEjemplares(self):
        """Dato de ejemplar:"""
        aux = request.env['library.ejemplar'].search([])
        ejemplares = []
        for ejemplares in aux:
            data.append({
                #ID del ejemplar.
                'ID': ejemplares.id,
                #Código del ejemplar.
                'Codigo': ejemplares.ejemplar_id,
                #Nombre del ejemplar.
                'Nombre': ejemplares.titulo_id,
                #Fecha de devolución (si aplica).
                'Fecha de devolucion': ejemplares.fecha,
            })
        return aux
    
    @http.route('/library_book/informacion_ejemplar_panel', auth='user', type='json')
    def Ejemplar(self):
        aux = request.env['library.ejemplar'].browse(ejemplar_id)

        #si no existe el buscadp
        if ejemplar.()
            return {'error: ID no encontrado'}
        #Nombre del ejemplar.
        #Quien lo alquilo/compro.
        #Valor del ejemplar