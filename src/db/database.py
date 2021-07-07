import sqlite3

class Database:
	con = sqlite3.connect('database.db')
	cur = con.cursor()

	def create_database(self):
		try:
			self.cur.execute('CREATE TABLE accounts (email text, password text)')
			self.con.commit()
		except Exception as e:
			print(e)

	def insert_database(self, values={}):
		try:
			self.cur.execute('DELETE FROM accounts')
			email = values['email']
			password = values['password']
			self.cur.execute(f'INSERT INTO accounts VALUES ("{email}", "{password}")')
			self.con.commit()
		except Exception as e:
			print(e)

	def get_data(self):
		try:
			data=[]
			for row in self.cur.execute('SELECT * FROM accounts'):
				data.append({
					'email': row[0],
					'password': row[2]
				})
			return data
		except Exception as e:
			print(e)