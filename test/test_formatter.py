import unittest
from service.formatter import formatter


class ServiceFormatterTestCase(unittest.TestCase):
    def test_formating_from_list(self):
        original = {
                'Image': 'ubuntu', 'State': 'running', 'Names': ['/dreamy_knuth'],
                'Id': '4391ad187af1851641d0a48583c6d1166e8e79279a4bad319883dfa3c3f06a15',
                'Created': 1460683339
                }
        expected = {
                'id': '4391ad187af1',
                'name': 'dreamy_knuth',
                'state': 'running'
                }

        self.assertEqual(formatter(original), expected, "wrong result after format")

    def test_formating_from_inspect(self):
        original = {
                'Image': 'ubuntu', 'State': {'Status': 'running', 'Error': '', 'Dead': False}, 'Name': '/dreamy_knuth',
                'Id': '4391ad187af1851641d0a48583c6d1166e8e79279a4bad319883dfa3c3f06a15',
                'Created': 1460683339
                }
        expected = {
                'id': '4391ad187af1',
                'name': 'dreamy_knuth',
                'state': 'running'
                }

        self.assertEqual(formatter(original), expected, "wrong result after format")
