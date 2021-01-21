def greet_users(names):
    """向列表中的每位用户都发出问候"""
    for name in names:
        msg = "Hello " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'dd']
greet_users(usernames)
