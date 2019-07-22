from locker import Password, User
import random
import string


def create_password(name,password):
	    new_password = Password(name,password)
	    return new_password


def save_passwords(passwords)
	 passwords.savePassword()

def display_passwords():
	 return Password.display_passwords()

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def del_user(user):
	user.delete_user()   

def createCred(name, Password):
    new_user = User(name, Password)
    return new_user
def saveCredentials(details):
    details.saveUser()
def verify_user(first_name,password):
    
    checking_user = User.check_user(first_name,password)
    return checking_user    

		 



def main():
	

 while True:
        

        print("Hello Welcome to your password locker")
        print("Use either 1,2,exit to navigate. \n 1--Create a password lock account  \n 2--Log in \n exit--exit account")
        code = input(" Enter your choice ").lower()
        if code == "1":
                print("Enter Username")
                name = input()
                print("Enter referred password")
                password = input()
                saveCredentials(createCred(name,password))
                print(f"{name}, your credentials have been saved successfully")

        elif code == "exit":
            print("thank u and see u again.......")
            break        
        if code == "2":
            print("Enter user Name")
            name = input()
            print("Enter password")
            passw = input()
            user_exists = verify_user(name,passw)
            if user_exists == name:
                print(" ")
                print(f'Welcome {name}. Please choose an option to continue.')
                print(' ')


                while True:
                    print("Use these short codes : 1- create a new account, 2- check existing users, 3- Generate a password, 4- delete an account, 5-exit ")



                    short_code = input().lower()

                    if short_code == '1':
                            print("New password")
                            print("-"*10)
                            print("name")
                            name = input()

                            print("Password")
                            password = input()
                            save_passwords(create_password(name,password))
                            print ('\n')
                            print("password has been saved")
                            print ('\n')
		                    
                           



                   
                    elif short_code == '2':
                    	print("this is ur list")
                    	for password in display_passwords():
                    		print(f"{password.username},{password.Password}")

                    

                    elif short_code =='3':
                    	print("Enter account Name")
                    	name = input()
                    	password = randomString(8)
                    	save_passwords(create_password(name,password))

                    elif short_code == '4':
                    	print("Enter name of account to be deleted")
                    	deli_user = input()
                    	if display_passwords(deli_user):
                    		search_account = find_user(deli_user)
                    		del_user(search_account)
                    		print(f"{display_passwords} account credentials have been successfully deleted")	

                    
                    elif short_code == "5":
                    	print("thank u and see u again.......")
                    	break

         




if __name__ == '__main__':
	main()                            