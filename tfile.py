import unittest


def generat_sum_fibo(n):
    l = []
    a = 0
    b = 1
    for i in range(n):
        l.append(a)
        a, b = b, a + b
    return l

def returnTrue(n):
    return n


class TestFunction(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_general(self):
        self.assertEqual(generat_sum_fibo(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    
    def test_returnTrue(self):
        self.assertTrue(returnTrue(1))


if __name__ == '__main__':
    unittest.main()

