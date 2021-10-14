import hashlib
import yaml
from setup_db import DataBase as db



"""
This program asks the user for their username
and password. 
If the passord matches the username, then we give them access
If not we don't give them access.
"""

# Connect to the database
DB_NAME = "testDB.db"

db.create_connection(DB_NAME)


#Open and read data from the yaml config file
with open('cred.yaml','r') as f:
	V_CREDENTIALS = yaml.safe_load(f)




def is_valid_credentials(user_name, password_hash):
	"""
	Takes in the username and password 
	Returns true if credentials are correct.
	Returns false if credentials are not correct.
	"""


	check = False
	stored_user_cred = None
	# Check whether user name or password is valid
	for cred in V_CREDENTIALS:

		if cred['username'] == user_name and cred['password_hash'] == password_hash:
			stored_user_cred = cred
			check = True
			print("Access Granted")
			break

	if check == False:
		print("Access Denied, try again.")
		return login_cred()
		
		if stored_user_cred is None:
			return False


def login_cred():

	"""
	Ask user for login credentials

	"""
	user_name = input("Enter your username: ")
	password = input("Enter your password: ")
	password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
	is_valid_credentials(user_name, password_hash)






login = login_cred()

