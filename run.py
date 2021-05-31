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
 

