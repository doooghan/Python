import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    """测试雇员类"""

    def setUp(self):
        """默认雇员及工资"""
        self.my_employee = Employee('dd', 'h', 100)

    def test_give_default_raise(self):
        """测试年薪默认增加方法"""
        self.my_employee.give_raise()
        self.assertEqual(5100, self.my_employee.salary)

    def test_give_custom_raise(self):
        """测试其他量的年薪增量方法"""
        self.my_employee.give_raise(3000)
        self.assertEqual(3100, self.my_employee.salary)


if __name__ == '__main__':
    unittest.main()
