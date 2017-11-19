import unittest
import fin_tools.credit

class TestCredit(unittest.TestCase):

    def test_cds(self):
        cd = credit.cds(3, [1/1.1], [0.1], 0.75, 1000, 4, 0.1)
        calculated_price = cd.get_price()
        actual_price = 5.59
        self.assertAlmostEqual(calculated_price, actual_price, places=2)

    def test_cds_variable(self):
        cd = cds(3, [1/1.1, 1/1.11, 1/1.12], [0.1, 0.05, 0.025], 0.5, 1000, 4, 0.1)
        calculated_price = cd.get_price()
        actual_price = 18.98
        self.assertAlmostEqual(calculated_price, actual_price, places=2)

if __name__ == '__main__':
    unittest.main()