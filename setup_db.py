import hashlib
import sqlite3
from sqlite3 import Error

DB_NAME = "testDB.db"


class DataBase:
	def create_connection(DB_NAME):
		"""create a database connection to a SQlite database"""
		conn = None

		try:
			con = sqlite3.connect(DB_NAME)
			print("Connection Successful")

		except Error as e:
			print(e)
		finally:
			if conn:
				conn.close()