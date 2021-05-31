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
    
    while True:
        print("Create your account's credentials using the following short codes:\n cc-create a new credential \n DC-To display credential \n FC-To find credential \n CD-To delete crdential \n EX-To exit the app")
        short_code=input().lower()
        if short_code=='cc':
            print("Cretae new ccredential account")
            print('-'*10)
            print("Account name: ")
            accountName=input()
            print("Entrer your account username:")
            accountUsername=input()
            while True:
                print("Create the account password using the following short codes: TP to type your own password and GP - to be gnerated with a random password ")
                my_password=input().lower()
                if my_password=='tp':
                    accountPassword = input("Enter your preffered password")

                elif my_password=='gp':
                    my_password=generate_password()
                    break
                else:
                    print("invalid password")
            save_credentials(create_new_credentials(accountName, accountUsername, password))
            print('\n')
            print(f"Account Credential for: {accountName} - User Name: {accountUsername} - Password:{accountPassword} created succesfully")
            print('\n')
        elif short_code=='dc':
            if display_credentials():
                print("These are you accounts and credentials")
                print('*'*20)
                for account in display_credentials():
                    print(f"Account: {account.accountName}....User Name: {account.accountUsername}....Password: {account.accountPassword}")
                    print('*'*10)
            
            else:
                print("YOU DON'T HAVE ANY CREDENTIALS SAVED!!")

        elif short_code=='fc':
            print("Enter the account name you would wish to search for")     
            name=input().lower()
            if find_credentials(name):
                search_credential=find_credentials(name)
                print(f"Account name: {search_credential.accountName}")  
                print('*'*10)
                print(f"User Name: {search_credential.accountUserame}.... Password :{search_credential.accountPassword}")  

            else:
                print("The credentials you searched for does not exist")
                print('\n')
        
        


 

