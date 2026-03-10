from django.test import SimpleTestCase

class BasicSimpleTests(SimpleTestCase):
    def test_basic_math(self):
        self.assertEqual(3 * 3, 9)
