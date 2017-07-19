import sys,os
import unittest
sys.path.append(os.getcwd())
import lambda_function

class MyTest(unittest.TestCase):
    def setUp(self):
        pass
    def test_function_requirement_1(self):
        self.assertEquals(lambda_function.handler(None, None), True)
