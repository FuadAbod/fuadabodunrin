from Main_Calculation import bmi_calculator
import unittest
import timeit

class TestSum(unittest.TestCase):
    def test_the_number_of_overweight(self):
        result = bmi_calculator('test_data.json')
        self.assertEqual(result[1],2)
    
    def test_speed_of_function(self):
        directory='test_data.json'
        time_taken = timeit.timeit(stmt=str(bmi_calculator(directory)),number=1000000)
        self.assertLess(time_taken,3)
        
if __name__ == '__main__':
    unittest.main()