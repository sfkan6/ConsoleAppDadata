import sqlite3


class DataB:
    def __init__(self):
        self.conn, self.cur = self.connect()

    def connect(self):
        conn = sqlite3.connect('profile.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Profile
                      (id INTEGER UNIQUE, API_KEY TEXT, SECRET_KEY TEXT)''')
        conn.commit()
        return conn, cur

    def change_data(self, token, secret):
        self.cur.execute("INSERT OR REPLACE INTO Profile (id, API_KEY, SECRET_KEY)"
                         " VALUES ('%s', '%s', '%s')" % (0, token, secret))
        self.conn.commit()

    def return_data(self):
        data = self.cur.execute("SELECT API_KEY, SECRET_KEY FROM Profile ").fetchone()
        return data
