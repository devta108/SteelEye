import os
import unittest
from utils import get_document


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(get_document(None, None), None)  # add assertion here
        self.assertEqual(get_document(os.getenv('base_url'), None), None)
        self.assertEqual(get_document("https://github.com", "basic.xml"), None)
        self.assertEqual(get_document(os.getenv('base_url'), "basic.xml"), 'basic.xml')


if __name__ == '__main__':
    unittest.main()
