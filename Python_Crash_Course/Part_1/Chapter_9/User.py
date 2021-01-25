class User:
    """用户类"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """打印简要的用户信息"""
        print(self.full_name.title()+ " is " + str(self.age) + " years old this year.")

    def greet_user(self):
        """向用户发出个性化问候"""
        print("Hello, " + self.full_name.title())

    def get_login_attempts(self):
        """返回当前登陆尝试次数"""
        return self.login_attempts

    def increment_login_attempts(self):
        """增加登陆尝试次数"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """重置尝试登陆次数"""
        self.login_attempts = 0


user_1 = User("dong", "han", 18)
user_1.describe_user()
user_1.greet_user()

user_1.increment_login_attempts()
print(user_1.get_login_attempts())
user_1.increment_login_attempts()
print(user_1.get_login_attempts())
user_1.reset_login_attempts()
print(user_1.get_login_attempts())
