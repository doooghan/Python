import unittest

from Python_Crash_Course.Part_1.Chapter_11.name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, "Janis Joplin")


unittest.main()
