import sqlite3

class Database:
	def __init__(self, db_file):
		self.connection = sqlite3.connect(db_file, check_same_thread=False)		
		self.cursor = self.connection.cursor()

	def lang_ru(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE bot_userprofile SET language = ? WHERE user_id = ?", ("ru", user_id))
	
	def lang_en(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE bot_userprofile SET language = ? WHERE user_id = ?", ("en", user_id))
	
	def lang_ua(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE bot_userprofile SET language = ? WHERE user_id = ?", ("ua", user_id))