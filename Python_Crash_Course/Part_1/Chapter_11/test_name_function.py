import unittest

from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_something(self):
        self.assertEqual(True, False)

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, "Janis Joplin")


# 测试必须写在 main 里面, 或者在命令行执行
if __name__ == '__main__':
    unittest.main()
