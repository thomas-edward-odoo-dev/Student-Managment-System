# -*- coding: utf-8 -*-
from odoo import http

# class StudentTest(http.Controller):
#     @http.route('/student_test/student_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/student_test/student_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('student_test.listing', {
#             'root': '/student_test/student_test',
#             'objects': http.request.env['student_test.student_test'].search([]),
#         })

#     @http.route('/student_test/student_test/objects/<model("student_test.student_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('student_test.object', {
#             'object': obj
#         })