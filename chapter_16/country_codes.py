from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        if country_name == 'Yemen, Rep.':
            return 'ye'

    # 如果没找到国家就返回 None
    return None
