# -*- coding: utf-8 -*-
import time
from datetime import datetime
from odoo import fields, models, api, _
from odoo.exceptions import UserError, except_orm
from odoo import exceptions
from datetime import date
from dateutil.relativedelta import relativedelta


class SalaryAdvancePayment(models.Model):
    _inherit = "salary.advance"

    @api.one
    def submit_to_manager(self):
        first_number_of_days = 8
        period = [datetime.today().replace(day=x).date() for x in range(1, first_number_of_days)]
        if date.today() in period:
            self.state = 'submit'
        else:
            raise UserError(
                "Don't Panic!!!!!!!! You should ask your Salary Advance in first {} days of the month but today {}".format(
                    first_number_of_days, date.today()))
