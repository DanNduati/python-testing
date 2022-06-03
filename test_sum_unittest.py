import unittest

class TestSum(unittest.TestCase):
    #put tests into classes as methods
    def test_sum(self):
        self.assertEqual(sum([1,2,3]),6,"Should be 6")
        
    def test_sum_tuple(self):
        self.assertEqual(sum((1,2,2)),6,"Should be 5")
        
if __name__ == "__main__":
    unittest.main()