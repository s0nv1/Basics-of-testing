import unittest
import test


class NameTastCase(unittest.TestCase):
    
    def test_first_and_last_name(self):
        full = test.full_name('carl', 'johonson')
        full1 = test.full_name('cARL', 'jOHONSON')
        self.assertEqual(full, 'Carl Johonson')
        self.assertEqual(full1, 'Carl Johonson')


class SquareNum(unittest.TestCase):
    
    def test_square_num(self):
        l = [1, 2, 3, 4, 5]
        fun = test.squares(l)
        self.assertEqual(fun, [1, 4, 9, 16, 25])


unittest.main()
