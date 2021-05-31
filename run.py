from password import User, Credentials

def create_user_account(username, password):
    '''
    function to return new user account
    '''
    new_user=User(username,password)
    return new_user

def save_users(user):
    '''
    function to save user
    '''
    user.save_user()

def display_users():
    '''
    function to return all users saved
    '''
    return User.display_users()

def user_login(username, password):
    '''
    function to authenticate user login
    '''
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credentials(accountName, accountUsername, accountPassword):
    '''
    function to return new credentials 
    '''
    new_credentials=Credentials(accountName, accountUsername, accountPassword)
    return new_credentials

def save_credentials(credentials):
    '''
    function to save created credentials to the credentials list
    '''
    credentials.save_credentials()
    return credentials

def delete_credentials(credentials):
    '''
    function to delete credentials
    '''
    credentials.delete_credentials()
    
def find_credentials(account_name):
    '''
    function to find credentials using account_name
    '''
    return Credentials.find_credentials(account_name)

def credentials_exists(account_name):
    '''
    function to check existing credentials and return a boolean 
    '''
    return Credentials.credentials_exists(account_name)

def display_credentials():
    '''
    function that returns all credentials saved
    '''
    return Credentials.display_credentials()

def generate_password():
    '''
    function that genarates random passwords
    '''
    randon_password=Credentials.generate_password()
    return randon_password

def main():
    print("WELCOME TO PASSWORD LOCKER APP. \n To continue, please enter one of the following short codes: \n CA----Create new user Account \n AH----Already have an account? \n")
    short_code=input().lower()
    if short_code=="ca":
        print("Create your new user account")
        print('-'*20)
        username=input("Enter your Username: ")
        while True:
            print("Enter TP to type your own password or GP to generate a random password from the application")
            my_password= input().lower()
            if my_password=='tp':
                password= input("Enter your preffered password:.. ")
                break
            elif my_password=='gp':
                password=generate_password()
                break
            else:
                print("Please input a valid password and try again")
        save_users(create_user_account(username,password))
        print('*'*50)
        print(f"Your account was created successful,your username is {username} and your password is {password}")
        print('*'*50)

    elif short_code=="ha":
        print("*"*50)
        print("Enter your User name and your Password to sign in:")
        print("*"*50)
        username=input("Enter your user name: ")
        password= input("Please enter your password: ")
        sign_in=user_login(username,password)
        if user_login==sign_in:
            print(f"Hello {username}, welcome to your password locker app manager")
            print('\n')
            
                


 

