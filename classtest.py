import unittest
import class_ex



class TestCar(unittest.TestCase):
    
    def setUp(self):
        self.my_car = class_ex.Car('name', 'model', 2020, 'green')
    
    def test_repaint(self):
        self.assertEqual(self.my_car.color, 'green')
        self.my_car.repaint('black')
        self.assertEqual(self.my_car.color, 'black')
    
    def test_drive(self):
        self.assertEqual(self.my_car.km, 0)
        self.my_car.kilometr()
        self.assertEqual(self.my_car.km, 100)

unittest.main()
