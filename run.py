from password import User, Credentials
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=False)
print (Fore.RED + Back.WHITE + Style.BRIGHT +' some text')
def my_name():
    print("       __   ____     ____  ____   ____            _   _______             ____   ____    ")
    print("        |  /    \   /      |     |    \ |    |    /\     |         /\    |    \ |    \   ")
    print("        | |      |  \____  |___  |____/ |____|   /  \    |        /  \   |____/ |____/   ")
    print("        | |      |       \ |     |      |    |  /____\   |       /____\  |      |        ")
    print("     ___|  \____/    ____/ |___  |      |    | /      \  |      /      \ |      |        ")
my_name()
print('\n')

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

def create_new_credentials(account_name, account_username, account_password):
    '''
    function to return new credentials 
    '''
    new_credentials=Credentials(account_name, account_username, account_password)
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
    print("WELCOME TO PASSWORD LOCKER APP. \n To continue, please enter one of the following short codes: \n CA----Create new user Account \n AH----Already have an account? \n EX---to exit the application")
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
        print('\n')
        print('*'*50)
        print('\n')
        print(f"Your account was created successful,your username is {username} and your password is {password}")
        print('\n')
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

    elif short_code=="ex":
         print("THANK YOU FOR VISITING PASSWORD LOCKER APP")
    
    while True:
        print("Create your account's credentials using the following short codes:\n cc-create a new credential \n DC-To display credential \n FC-To find credential \n CD-To delete crdential \n EX-To exit the app")
        short_code=input().lower()
        if short_code=='cc':
            print('\n')
            print("Cretae new credential account")
            print('-'*10)
            print('\n')
            print("Account name: ")
            account_name=input()
            print('\n')
            print("Enter your account username:....")
            account_username=input()
            while True:
                print("Create the account password using the following short codes: TP to type your own password and GP - to be gnerated with a random password ")
                my_password=input()
                if my_password=='tp':
                    account_password= input("Enter your preffered password: ")

                elif my_password=='gp':
                    account_password=generate_password()
                    break

                else:
                    print("invalid choice for creating password")
                    
            save_credentials(create_new_credentials(account_name, account_username, account_password))
            print('\n')
            print(f"Account Credential for: {account_name}  User Name: {account_username} - Password:{account_password} was created succesfully")
            print('\n')

        elif short_code=='dc':
            if display_credentials():
                print("These are you accounts and their respective credentials")
                print('\n')
                print('*'*20)
                for account in display_credentials():
                    print(f"Account Name: {account.account_name}....Account User Name: {account.account_username}....Account Password: {account.account_password}")
                    print('*'*10)
            
            else:
                print("YOU DON'T HAVE ANY CREDENTIALS SAVED!!")

        elif short_code=='fc':
            print("Enter the account name you would wish to search for")     
            name=input()
            if find_credentials(name):
                search_credential=find_credentials(name)
                print(f"Account name: {search_credential.account_name}")  
                print('*'*10)
                print(f"User Name: {search_credential.account_username}.... Password :{search_credential.account_password}")  

            else:
                print("The credentials you searched for does not exist")
                print('\n')

        elif short_code=='cd':
            print("Enter the account you want to delete")
            name=input()
            if find_credentials(name):
                search_credential=find_credentials(name)
                print('\n')
                search_credential.delete_credentials()
                print('\n')
                print(f"Your credentials for {search_credential.account_name} have been deleted successfully")

            else:
                print("The credentials you want to delete do not exist")

        elif short_code == 'ex':
            print("Thanks for using password locker app")
            break

        else:
            print("Wrong entries, Please review the short codes to help you!!")
        
        
if __name__=='__main__':
    main()

 

