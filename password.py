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


    
        