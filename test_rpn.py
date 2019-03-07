import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
        result = rpn.calculate('2 2 ^')
        self.assertEqual(4, result)
        result = rpn.calculate('2 3 ^')
        self.assertEqual(8, result)


# TestBasics tb;
# tb.test_add() ==> TestBasics.test_add(tb)
