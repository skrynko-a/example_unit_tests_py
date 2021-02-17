import unittest

from pyOlolo.App.SimpleClass import SimpleClass


class TestSimpleClassUnit(unittest.TestCase):

    def test_check_text_from_console_by_none(self):
        result = SimpleClass.check_text_from_console(None)
        self.assertFalse(result, "Для значения None метод отработал некорректно")

    def test_check_text_from_console_by_empty_string(self):
        result = SimpleClass.check_text_from_console("")
        self.assertFalse(result, "Для пустой строки метод отработал некорректно")

    def test_check_text_from_console_by_non_empty_string(self):
        result = SimpleClass.check_text_from_console('something')
        self.assertTrue(result, "Для значения something метод отработал некорректно")