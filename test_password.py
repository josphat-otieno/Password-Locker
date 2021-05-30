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

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list=[]

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

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list=[]    

    def test_init(self):
        '''
        test case to confirm if credentials objects is intialised correctly
        '''
        self.assertEqual(self.new_credentials.account_name,'Facebook')
        self.assertEqual(self.new_credentials.account_username,'Josphato')
        self.assertEqual(self.new_credentials.account_password,'jose!!otieno@45')

    def test_save_credentials(self):
        '''
        test case to test if the credentials are saved into the credentilas list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        '''
        test case to confirm if multiple credentilas can be saved into credentials list
        '''
        self.new_credentials.save_credentials()
        new_account=Credentials("Twitter","josephat_otieno", "joseotis45")
        new_account.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        '''
        delete_crdentials case to test if we can delete a credential
        '''
        self.new_credentials.save_credentials()
        new_account=Credentials("Twitter","josephat_otieno", "joseotis45")
        new_account.save_credentials()

        self.new_credentials.delete_credentials() 
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        self.new_credentials.save_credentials()
        new_account= Credentials("Twitter","josephat_otieno", "joseotis45")
        new_account.save_credentials()

        found_credential= Credentials.find_credentials("Twitter")

        self.assertEqual(found_credential.account_name,new_account.account_name)

    def test_credentials_exists(self):
        '''
        test to check if we can return a boolean if we 
        cannot find a credentials using the account name"
        '''
        self.new_credentials.save_credentials()
        new_account= Credentials("Twitter","josephat_otieno", "joseotis45")
        new_account.save_credentials()

        credentials_exists=Credentials.credentials_exists("Twitter")

        self.assertTrue(credentials_exists)
       
       
        
if __name__=='__main__':
    unittest.main()



