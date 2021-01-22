def build_profile(first, last, *args, **user_info):
    """创建一个字典,其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for item in args:
        print(item)
    for key, value in user_info.items():
        profile[key] = value

    return profile


user_profile = build_profile('albert', 'einstein', 'abv', 'hhh', location='princeton', field='physics')

print(user_profile)
