# unittests for main.py
# import unittest module
import unittest
# import the function to be tested
from main import check_input, is_win

# write a class to test the function
class TestMain(unittest.TestCase):
    
    # test the check_input function
    def test_check_input(self):
        # test the function with valid input
        self.assertEqual(check_input('r'), True)
        self.assertEqual(check_input('p'), True)
        self.assertEqual(check_input('s'), True)
        # test the function with invalid input
        self.assertEqual(check_input('a'), False)
        self.assertEqual(check_input('b'), False)
        self.assertEqual(check_input('c'), False)
    
    # test the is_win function
    def test_is_win(self):
        # test the function with user wins
        self.assertEqual(is_win('r', 's'), True)
        self.assertEqual(is_win('s', 'p'), True)
        self.assertEqual(is_win('p', 'r'), True)
        # test the function with computer wins
        self.assertEqual(is_win('s', 'r'), False)
        self.assertEqual(is_win('p', 's'), False)
        self.assertEqual(is_win('r', 'p'), False)

# run the test
if __name__ == '__main__':
    unittest.main()