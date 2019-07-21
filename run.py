from locker import Password
import random
import string


def create_password(name,password):
	    new_password = Password(name,password)
	    return new_password


def save_passwords(passwords):
	 passwords.savePassword()

def display_passwords():
	 return Password.display_passwords()

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def del_user(user):
	user.delete_user()   

		 



def main():
	print("Hello Welcome to your password locker. What is your name?")
	user_name = input()
	print(f"Hello {user_name}. what would you like to do?")
	print('\n')
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