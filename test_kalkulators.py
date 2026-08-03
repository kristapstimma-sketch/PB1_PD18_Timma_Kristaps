import unittest
from kalkulators import saskaitit

class TestKalkulators(unittest.TestCase):
    def test_saskaitit(self):
        self.assertEqual(saskaitit(2, 3), 5)
        self.assertEqual(saskaitit(-1, 1), 0)
        self.assertEqual(saskaitit(0, 0), 0)

if __name__ == '__main__':
    unittest.main()