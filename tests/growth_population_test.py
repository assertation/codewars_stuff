import unittest

from src.growth_population import nb_year


class GrowthPopulationTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(nb_year(1500, 5, 100, 5000), 15)
        self.assertEqual(nb_year(1500000, 2.5, 10000, 2000000), 10)
        self.assertEqual(nb_year(1500000, 0.25, 1000, 2000000), 94)


if __name__ == "__main__":
    unittest.main()
