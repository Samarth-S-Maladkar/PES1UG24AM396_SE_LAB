import unittest
from self_storage import rent_due, access_allowed, payment_status


class TestSelfStorageBranchCoverage(unittest.TestCase):
    def test_unknown_unit_size_raises(self):
        with self.assertRaises(ValueError):
            rent_due("invalid_size", 2, False, False)

    def test_negative_months_raises(self):
        with self.assertRaises(ValueError):
            rent_due("small", -2, False, False)

    def test_within_deposit_months(self):
        self.assertEqual(rent_due("small", 1, False, False), 0)

    def test_member_large_unit_no_extra_covered_month(self):
        self.assertEqual(rent_due("large", 5, False, True), 160)

    def test_member_small_unit_climate_short_extra(self):
        self.assertEqual(rent_due("small", 5, True, True), 360)

    def test_climate_long_extra_discount(self):
        self.assertEqual(rent_due("small", 9, True, False), 840)

    def test_non_climate_long_extra_discount(self):
        self.assertEqual(rent_due("small", 9, False, False), 560)

    def test_access_owner_within_limit(self):
        self.assertTrue(access_allowed(1, 4, True))

    def test_access_owner_exceeds_limit(self):
        self.assertFalse(access_allowed(14, 5, True))

    def test_access_non_owner_early_morning_denied(self):
        self.assertFalse(access_allowed(5, 1, False))

    def test_access_non_owner_late_night_denied(self):
        self.assertFalse(access_allowed(23, 1, False))

    def test_access_non_owner_valid_hours_allowed(self):
        self.assertTrue(access_allowed(12, 2, False))

    def test_access_non_owner_too_many_visitors(self):
        self.assertFalse(access_allowed(12, 3, False))

    def test_payment_autopay_no_prior_late_current(self):
        self.assertEqual(payment_status(0, True, False), "current")

    def test_payment_manual_prior_late_grace(self):
        self.assertEqual(payment_status(0, False, True), "grace")

    def test_payment_manual_no_prior_late_lien(self):
        self.assertEqual(payment_status(-11, False, False), "lien")


if __name__ == "__main__":
    unittest.main()
