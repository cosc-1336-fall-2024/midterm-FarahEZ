#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_a.question_a import reverse_string
from src.question_b.question_b import is_prime
from src.question_c.question_c import get_person_category
from src.question_d.question_d import get_day_of_week

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())
    
    def test_reverse_string(self):
        self.assertEqual("dlrow olleh", reverse_string("hello world"))
    
    def test_is_prime(self):
        self.assertEqual(False, is_prime(4))
        self.assertEqual(True, is_prime(5))
        self.assertEqual(True, is_prime(11))
    
    def test_get_person_category(self):
        self.assertEqual("infant", get_person_category(1))
        self.assertEqual("child", get_person_category(2))
        self.assertEqual("teenager", get_person_category(14))
        self.assertEqual("adult", get_person_category(31))
    
    def test_get_day_of_week(self):
        self.assertEqual("Invalid number", get_day_of_week(0))
        self.assertEqual("Monday", get_day_of_week(1))
        self.assertEqual("Tuesday", get_day_of_week(2))
        self.assertEqual("Wednesday", get_day_of_week(3))
        self.assertEqual("Invalid number", get_day_of_week(8))

        


