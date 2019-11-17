from odoo import models, fields, api
from datetime import datetime


class wiz_calc_age(models.TransientModel):
    _name = "wiz.calc.age"
    
    from_date = fields.Date("From Date", required=True)
    to_date = fields.Date("To Date", required=True)
    
    @api.multi
    def calc_age(self):
        student_obj = self.env['student.student']
        for rec in self:
            students = student_obj.search([('dob', '>=', rec.from_date), ('dob', '<=', rec.to_date)])

            for student in students:
                dob = student.dob
                if dob:
                    student.age = (datetime.now() - datetime.strptime(str(dob), '%Y-%m-%d')).days / 365
        return True