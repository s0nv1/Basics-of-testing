import unittest
import tfun


class TestFunction(unittest.TestCase):
    
    def test_func(self):
        result = tfun.function([1, 2, 3, 4, 5])
        self.assertEqual(result, 15)
    
    def test_wrapper(self):
        result = tfun.wrapper([1, 2, 3, 4, 5])
        self.assertEqual(result, 55)
        


class TestCarNow(unittest.TestCase):
    
    def setUp(self):
        self.car = tfun.Bus('name', 12, 199, 'black')
    
    def test_km(self):
        self.assertEqual(self.car.km, 199)
        self.car.set_km(100)
        self.assertEqual(self.car.km, 100)
    
    def test_color(self):
        self.assertEqual(self.car.color, 'black')
        self.car.set_color('yellow')
        self.assertEqual(self.car.color, 'yellow')
    
    def test_age(self):
        self.assertEqual(self.car.age, 12)
        self.car.set_age()
        self.assertEqual(self.car.age, 13)
        
unittest.main()
