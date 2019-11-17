##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be>).
#    Serpent Consulting Services Pvt. Ltd.
#    Copyright (C) 2014-2015 Serpent Consulting Services Pvt. Ltd. (<http://www.serpentcs.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warradegreesty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
#    Module: Student Registration Management for College or University
#    Description: Demo Generated for purpose of ODOO 9 Technical Training in Arabic
#    Author: Serpent Consulting Services Pvt. Ltd.
#    Date: November 2015
#
##############################################################################

from odoo import models, fields

class student_audit_log(models.Model):
    _name = "student.audit.log"
    
    user_id = fields.Integer("User ID")
    date = fields.Datetime("Date")
    student_info = fields.Char("Student")
    status = fields.Selection([('create', 'Created'),('write','Updated'),('delete','Deleted'),('copy','Copied')], "Status")
    