import unittest
from unittest.mock import Mock, mock_open, patch


def file_parser(file, find_string, replace_string=None):
    if not file:
        raise FileNotFoundError
    f = open(file, 'r')
    text = f.read()
    if not replace_string:
        count = text.count(find_string)
        return f'Found {count} strings'
    if replace_string:
        count = text.count(find_string)
        swap = text.replace(find_string, replace_string)
        w = open(file, 'w')
        w.write(text)
        return f'Replaced {count} strings'


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.moc = Mock(file="root.txt")
        self.moc_file = Mock()
        self.moc_file.file_parcer.return_value = "Replaced 5 strings"

    @unittest.expectedFailure
    def test_read_file(self):
        self.assertFalse(file_parser(self.moc.file, 'root'))

    def test_func_return(self):
        expected1 = "Replaced 5 strings"
        expected2 = 1
        self.assertEqual(expected1, self.moc_file.file_parcer("root.txt", "root", "toor"))
        self.assertEqual(expected2, self.moc_file.file_parcer.call_count)

    def test_get_file(self):
        with patch("__main__.open", mock_open(read_data="data")):
            expect = "Replaced 2 strings"
            self.assertEqual(expect, file_parser("1.txt", "a", 'o'))

    def test_number_of_call_count(self):
        self.assertEqual(0, self.moc_file.file_parcer.call_count)

    def tearDown(self):
        self.moс = None
        self.moc_file = None
