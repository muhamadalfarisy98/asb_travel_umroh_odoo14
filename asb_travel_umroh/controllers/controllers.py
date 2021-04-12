# -*- coding: utf-8 -*-
# from odoo import http


# class AsbTravelUmroh(http.Controller):
#     @http.route('/asb_travel_umroh/asb_travel_umroh/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asb_travel_umroh/asb_travel_umroh/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('asb_travel_umroh.listing', {
#             'root': '/asb_travel_umroh/asb_travel_umroh',
#             'objects': http.request.env['asb_travel_umroh.asb_travel_umroh'].search([]),
#         })

#     @http.route('/asb_travel_umroh/asb_travel_umroh/objects/<model("asb_travel_umroh.asb_travel_umroh"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asb_travel_umroh.object', {
#             'object': obj
#         })
