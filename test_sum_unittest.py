import unittest

#function to test
def add_iter(obj):
    if len(obj)>3:
        #add only 3 items
        raise ValueError("Limit reached")
    return sum(obj)

class TestSum(unittest.TestCase):
    #put tests into classes as methods
    def test_sum(self):
        self.assertEqual(add_iter([1,2,3]),6,"Should be 6")
        
    def test_sum_tuple(self):
        self.assertEqual(add_iter((1,2,2)),6,"Should be 5")
    
    def test_sum_exception(self):
        too_many_items = [1,2,3,4]
        with self.assertRaises(ValueError) as exception_context:
            add_iter(too_many_items)
        self.assertEqual(str(exception_context.exception),"Limit reached")

if __name__ == "__main__":
    unittest.main()