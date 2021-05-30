import unittest
from password import Credentials, User 
class TestUser(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('JosphatOtieno','jose@otis45')

    def test_init(self):
        '''
        test case to test if the object user is initialised correctly
        '''
        self.assertEqual(self.new_user.username,'JosphatOtieno')
        self.assertEqual(self.new_user.password,'jose@otis45')

    def test_save_user(self):
        '''
        test case to test if the user is saved into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_users(self):
        '''
        test case to confirm if we can save multiple users
        '''
        self.new_user.save_user()
        another_user=User("RoseGift","gift@rose")
        another_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_users(),User.user_list)

class TestCredentials(unittest.TestCase):
    '''
    A Test class that defines test cases for the Creentials  class.
    '''

    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_credentials = Credentials("Facebook","Josphato","jose!!otieno@45")

    def test_init_credentials(self):
        '''
        test case to confirm if credentials objects is intialised correctly
        '''
        self.assertEqual(self.new_credentials.account_name,'Facebook')
        self.assertEqual(self.new_credentials.account_username,'Facebook')
        self.assertEqual(self.new_credentials.account_password,'Facebook')



