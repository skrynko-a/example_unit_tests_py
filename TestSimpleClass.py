import pytest

from pyOlolo.App.SimpleClass import SimpleClass


class TestSimpleClass:

    @pytest.mark.parametrize("text", [None, ""])
    def test_check_text_from_console_by_empty_string(self, text):
        result = SimpleClass.check_text_from_console(text)
        assert not result, "Для значения " + text + " метод отработал некорректно"


    @pytest.mark.parametrize("text", ["some string"])
    def test_check_text_from_console_by_non_empty_string(self, text):
        result = SimpleClass.check_text_from_console(text)
        assert result, "Для значения " + text + " метод отработал некорректно"


