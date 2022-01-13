import unittest
import proj7

class TestMyStuff(unittest.TestCase):

    def test_fixType(self):
        self.assertEqual(proj7.fixType("PART"),"Part")
    def test_fixPartNumber(self):
        self.assertEqual(proj7.fixPartNumber("DO0OO432"), "D0000432")
    def test_fixDescription(self):
        self.assertEqual(proj7.fixDescription("PassengerDoorHandle"), "Passenger Door Handle")
    def test_fixQuantity(self):
        self.assertEqual(proj7.fixQuantity("10"), int(10))
    def test_fixLocation(self):
        self.assertEqual(proj7.fixLocation("Shop 15"), "Shop15")
    def test_fixCost(self):
        self.assertEqual(proj7.fixCost("$12,112.99"), float(12112.99))
    def test_fixPrice(self):
        self.assertEqual(proj7.fixPrice("$499"), float(499))
    def test_fixMake(self):
        self.assertEqual(proj7.fixMake("Honda"), "Honda")
    def test_fixModel(self):
        self.assertEqual(proj7.fixModel("Civic"), "Civic")
    def test_fixYearStart(self):
        self.assertEqual(proj7.fixYearStart(["2011","2013"]), int(2011))
    def test_fixYearEnd(self):
        self.assertEqual(proj7.fixYearEnd(["2011","2013"]), int(2013))
        
def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMyStuff)
    unittest.TextTestRunner(verbosity = 2).run(suite)

main()
