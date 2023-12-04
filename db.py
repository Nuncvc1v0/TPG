import sqlite3

class Database:
	def __init__(self, db_file):
		self.connection = sqlite3.connect(db_file, check_same_thread=False)		
		self.cursor = self.connection.cursor()

	def lang_ru(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE bot_userprofile SET language = ? WHERE user_id = ?", ("Русский", user_id))
	
	def lang_en(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE bot_userprofile SET language = ? WHERE user_id = ?", ("English", user_id))
	
	def lang_ua(self, user_id):
		with self.connection:
			return self.cursor.execute("UPDATE bot_userprofile SET language = ? WHERE user_id = ?", ("Український", user_id))

	def g_sum(self, current_date):
		with self.connection:
			# list = []
			idp = self.cursor.execute("SELECT amount FROM bot_giveaways WHERE date = ?", (current_date,))
			sums = [i for i in self.cursor.fetchall()]
			sumss = sum(sum(tuple_) for tuple_ in sums)
			return sumss

	def g_link(self, current_date):
		with self.connection:
			text_in_list = self.cursor.execute("SELECT ch_link FROM bot_giveaways WHERE date = ?", (current_date,)).fetchall()
			amount_in_list = self.cursor.execute("SELECT amount FROM bot_giveaways WHERE date = ?", (current_date,)).fetchall()

			list_l = [tuple_[0] for tuple_ in text_in_list]
			list_a = [tuple_[0] for tuple_ in amount_in_list]
			x = ['x' + str(item) for item in list_a]

			con = list(zip(list_l, x))	
			result_strings = [f"{url} {multiplier}" for url, multiplier in con]
			links_string = '\n'.join(result_strings)
			return links_string

	def g_sum_t(self, next_date):
		with self.connection:
			# list = []
			idp = self.cursor.execute("SELECT amount FROM bot_giveaways WHERE date = ?", (next_date,))
			sums = [i for i in self.cursor.fetchall()]
			sumss = sum(sum(tuple_) for tuple_ in sums)
			return sumss
	def g_link_t(self, next_date):
		with self.connection:
			text_in_list = self.cursor.execute("SELECT ch_link FROM bot_giveaways WHERE date = ?", (next_date,)).fetchall()
			amount_in_list = self.cursor.execute("SELECT amount FROM bot_giveaways WHERE date = ?", (next_date,)).fetchall()

			list_l = [tuple_[0] for tuple_ in text_in_list]
			list_a = [tuple_[0] for tuple_ in amount_in_list]
			x = ['x' + str(item) for item in list_a]

			con = list(zip(list_l, x))	
			result_strings = [f"{url} {multiplier}" for url, multiplier in con]
			links_string = '\n'.join(result_strings)
			return links_string