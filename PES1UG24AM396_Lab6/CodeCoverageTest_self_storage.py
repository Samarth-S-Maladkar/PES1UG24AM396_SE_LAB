import unittest
from self_storage import rent_due, access_allowed, payment_status


class TestSelfStorageCodeCoverage(unittest.TestCase):
    def test_within_deposit_months(self):
        self.assertEqual(rent_due("small", 1, False, False), 0)

    def test_unknown_unit_size_raises(self):
        with self.assertRaises(ValueError):
            rent_due("extra_large", 3, False, False)

    def test_negative_months_raises(self):
        with self.assertRaises(ValueError):
            rent_due("small", -1, False, False)

    def test_member_climate_long_term(self):
        self.assertEqual(rent_due("medium", 11, True, True), 840)

    def test_non_member_non_climate_short_term(self):
        self.assertEqual(rent_due("small", 4, False, False), 240)

    def test_access_allowed_owner(self):
        self.assertTrue(access_allowed(2, 3, True))

    def test_access_denied_after_hours(self):
        self.assertFalse(access_allowed(23, 1, False))

    def test_access_allowed_regular_hours(self):
        self.assertTrue(access_allowed(12, 1, False))

    def test_payment_status_autopay_prior_late_current(self):
        self.assertEqual(payment_status(12, True, True), "current")

    def test_payment_status_manual_grace(self):
        self.assertEqual(payment_status(5, False, True), "grace")

    def test_payment_status_lien(self):
        self.assertEqual(payment_status(-20, False, True), "lien")


if __name__ == "__main__":
    unittest.main()
