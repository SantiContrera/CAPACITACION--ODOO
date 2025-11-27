from odoo import http
from odoo.http import request

class EjemplarControlador(http.Controller):

    @http.route('/library_book/informacion_ejemplares', auth='public', type='http')
    def obtener_ejemplares(self):
        ejemplares = request.env['library.ejemplar'].sudo().search([])

        result = []
        for e in ejemplares:
            result.append({
                'id': e.id,
                'codigo': e.ejemplar_id,
                'nombre': e.titulo_id.display_name if e.titulo_id else False,
                'fecha_de_devolucion': e.fecha.isoformat() if e.fecha else False,
            })

        #para retornar como json 
        import json
        return request.make_response(
            json.dumps(result),
            headers=[('Content-Type', 'application/json')]
        )

    @http.route('/library_book/informacion_ejemplares/<int:ejemplar_id>', auth='public', type='http')
    def obtener_ejemplar(self, ejemplar_id):
        aux = request.env['library.ejemplar'].sudo().browse(ejemplar_id)

        if not aux.exists():
            return request.make_response(
                '{"error": "ID no encontrado"}',
                headers=[('Content-Type', 'application/json')]
            )

        template = request.env.ref('library_book.plantilla_ejemplar', raise_if_not_found=False)
        if template:
            print("Template OK") #ver si tiene un registro valido

        import json
        return request.make_response(
            json.dumps({
                'ejemplar': aux.ejemplar_id,
                'propietario': aux.propietario_id.name if aux.propietario_id.name else False,
                'precio': aux.precio,
            }),
            headers=[('Content-Type', 'application/json')]
        )

