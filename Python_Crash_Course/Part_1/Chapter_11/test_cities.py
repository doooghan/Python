import unittest

from city_functions import get_formatted_city


class CityTestCase(unittest.TestCase):
    """测试城市名字是否返回预期"""

    def test_city_country(self):
        """正确返回城市和国家"""
        city_name = get_formatted_city('santiago', 'chile')
        self.assertEqual(city_name, "Santiago, Chile - population 500000")

    def test_city_country_population(self):
        """返回正确的内容及人数"""
        name = get_formatted_city('beijing', 'china', population=30000000)
        self.assertEqual(name, "Beijing, China - population 30000000")


if __name__ == '__main__':
    unittest.main()
