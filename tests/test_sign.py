import unittest
from sign.get_name import get_with_space, get_no_space

class TestSign(unittest.TestCase):
    def test_with_space(self):
        self.assertEqual(get_with_space('-'), 'minus')
        self.assertEqual(get_with_space('/'), 'slash')
    
    def test_no_space(self):
        self.assertEqual(get_no_space('-'), 'minus')
        self.assertEqual(get_no_space('/'), 'slash')

if __name__ == '__main__':
    unittest.main()

