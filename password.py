class User:
    '''
    class that generates new instances of users
    '''
    user_list=[]
    '''
    empty user list
    '''

    def __init__(self, username,password):
        '''
        A method to define properties of a user
        args:
            username
            password
        '''
        self.username=username
        self.password=password

    def save_user(self):
        '''
        save user method to save user objects
        '''
        User.user_list.append(self)

    @classmethod
    def display_users(cls):
        '''
        dispaly method to dispaly user in a list
        '''
        return cls.user_list

class Credentials:
    '''
    class that generates new instances of credentials
    '''

    credentials_list=[]

    def __init__(self, account_name, account_username, account_password):
        '''
        A method to define properties of a user credenntials
        args:
            account_name
            account_username
            account_password  
        '''
        self.account_name=account_name
        self.account_username=account_username
        self.account_password=account_password

    def save_credentials(self):
        '''
        method to save credentials objects into credentials list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete credentials method deletes credentials saved from the credentials list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_credentials(cls, account_name):
        '''
        Method takes in a acount name and returns the credentials that matches that account.

        Args:
            acoount name: account name to search for
        Returns :
            returns the credentials that matches that account name.
        '''
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential



        




         


    


    
        