class Password:

    my_list = []
#create username and password
    def __init__(self,username,Password):
        self.username = username
        self.Password = Password
#create a save password
    def savePassword(self):
        Password.my_list.append(self) 


    def delete_user(self):
        User.user_list.remove(self)

    @classmethod
    def display_passwords(cls):
        return cls.my_list

    @classmethod
    def user_exists(cls,account):
        for user in cls.user_list:
            if user.account == account:
                return True
                return False

class User:
    user_list = []
    def __init__(self, name, Password):
        self.name = name
        self.Password = Password
    def saveUser(self):
        User.user_list.append(self)
    @classmethod
    def check_user(cls,name,Password):
        current_user = ''
        for user in User.user_list:
            if (user.name == name and user.Password == Password):
                current_user = user.name
                return current_user


    
 






