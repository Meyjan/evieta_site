# -*- coding: utf-8 -*-
from odoo import http

class EvietaSite(http.Controller):
    @http.route('/evieta_site/evieta_site/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/evieta_site/evieta_site/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('evieta_site.listing', {
            'root': '/evieta_site/evieta_site',
            'objects': http.request.env['evieta_site.evieta_site'].search([]),
        })

    @http.route('/evieta_site/evieta_site/objects/<model("evieta_site.evieta_site"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('evieta_site.object', {
            'object': obj
        })