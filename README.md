# Password Locker
## This is a Python application that allows a user to generate and store passwords for various accounts. It helps the user not forget their passwords and usernames for various accounts.

## By **[JOSEPHAT OTIENO](https://github.com/josphat-otieno)**

## Description
This is a Python application that allows a user to generate and store passwords for various accounts owned by the user. The application runs on the terminal and the user navigates through the app by using short codes. <br/>
The short codes are:
* ca - create Password Locker account
* ha- log into Pasword Locker account
* cc - creating  credentials for different accounts
* dc - display credentials for the logged in user
* fc - finding the existing user credentials for the logged in user accounts
* cd - deleting user credentials
* ex - exit from password locker account and also exit the terminal app


## Behaviour Driven Development
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Create an account | User Name : Josephat <br/> Password : jose | An account is created |
| Display account names | N/A | Display a list of user names for Password Locker accounts |
| Log into an account | User Name : John <br/> Password : doe | Log into the users account |
| Store existing log in credential | Account : gmail <br/> Password : jose | Create and save the user's credentials | 
| Generate a password for a new credential | Account : Password Locker | Generate a password for the user. <br/> Create and save the user's credential with the generated password | 
| Log out | N/A | Log out of Password Locker account |

## Prerequisites
* Python3.8

## Setup/Installation Requirements
* Clone [this repository](https://github.com/josphat-otieno/Password-Locker.git)  using the following commamnd  in the terminal: `git clone https://github.com/josphat-otieno/Password-Locker.git`. 
* Note:<em>You will need to git installed in your machine. You can install using the following comman: `$ sudo apt-get install git.`</em>
* After cloning, navigate to the folder where the repo was cloned and open it with your favorite code editor and run the `run.py` file to interact with the application using the following command `$python3.8 run.py`
* Run test_password.py to   run the test units using the following command `$python3.8 test_password.py`
## Known Bugs

No known bugs

## Technologies Used
- Python3.8

## Contacts
# Tel: +254717878813
Email: josephat.otieno@student.moringaschool.com


