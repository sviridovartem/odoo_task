from odoo.tests import TransactionCase
from odoo.addons.ohrms_salary_advance.models import salary_advance
from freezegun import freeze_time
from datetime import datetime, date
from odoo.exceptions import UserError


class DateTest(TransactionCase):

    @freeze_time('2019-01-10')
    def test_when_date_more_then_five_days_and_not_correct(self):
        user = self.env["salary.advance"].search([["state", "=", None]])[0]
        self.assertEqual(datetime.today().strftime("%Y-%m-%d"), '2019-01-10')
        with self.assertRaises(UserError):
            salary_advance.SalaryAdvancePayment.submit_to_manager(user)

    @freeze_time('2019-01-03')
    def test_when_date_less_then_five_days_and_correct(self):
        user = self.env["salary.advance"].search([["state", "=", None]])[0]
        self.assertEqual(datetime.today().strftime("%Y-%m-%d"), '2019-01-03')
        self.assertEqual(salary_advance.SalaryAdvancePayment.submit_to_manager(user), [None])
