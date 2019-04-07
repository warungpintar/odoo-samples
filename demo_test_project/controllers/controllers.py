# -*- coding: utf-8 -*-
from odoo import http

# class WpModule(http.Controller):
#     @http.route('/wp_module/wp_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wp_module/wp_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wp_module.listing', {
#             'root': '/wp_module/wp_module',
#             'objects': http.request.env['wp_module.wp_module'].search([]),
#         })

#     @http.route('/wp_module/wp_module/objects/<model("wp_module.wp_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wp_module.object', {
#             'object': obj
#         })