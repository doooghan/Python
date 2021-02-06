def get_formatted_city(city, country, population=500000):
    """返回整洁的城市名和国家人数"""
    full_city_name = "%s, %s" % (city, country)
    full_name = "%s - population %s" % (full_city_name.title(), population)
    return full_name
