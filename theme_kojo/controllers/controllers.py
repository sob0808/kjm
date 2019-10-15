# -*- coding: utf-8 -*-
from odoo import http

# class ThemeKojo(http.Controller):
#     @http.route('/theme_kojo/theme_kojo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/theme_kojo/theme_kojo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('theme_kojo.listing', {
#             'root': '/theme_kojo/theme_kojo',
#             'objects': http.request.env['theme_kojo.theme_kojo'].search([]),
#         })

#     @http.route('/theme_kojo/theme_kojo/objects/<model("theme_kojo.theme_kojo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('theme_kojo.object', {
#             'object': obj
#         })