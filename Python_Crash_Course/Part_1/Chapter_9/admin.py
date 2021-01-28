from Python_Crash_Course.Part_1.Chapter_9.user import User


class Privileges():
    """权限类"""

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """展示管理员的特殊权限"""
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """特殊的用户"""

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privilege = Privileges()


hd = Admin("dong", "h", 18)
hd.describe_user()
hd.greet_user()
hd.privilege.show_privileges()
