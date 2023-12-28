import sqlite3

class BotDB:
    def __init__(self, database_name='BotDB.db'):
        self.db = sqlite3.connect(database_name)
        self.cursor = self.db.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                name TEXT,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS admins (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                name TEXT,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS anime (
                id INTEGER PRIMARY KEY,
                name TEXT,
                link TEXT,
                series TEXT,
                options TEXT,
                description TEXT,
                img_url TEXT
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS viewed (
                id INTEGER PRIMARY KEY,
                name TEXT,
                link TEXT,
                series TEXT,
                options TEXT,
                description TEXT,
                img_url TEXT
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS favorites (
                id INTEGER PRIMARY KEY,
                name TEXT,
                link TEXT,
                series TEXT,
                options TEXT,
                description TEXT,
                img_url TEXT
            )
        ''')
        
        self.db.commit()

    def new_user(self, user_id, name):
        user_exists = self.cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)).fetchone()
        if not user_exists:
            self.cursor.execute('INSERT INTO users (user_id, name) VALUES (?, ?)', (user_id, name))
            self.db.commit()
        else:
            self.cursor.execute("UPDATE users SET name = ? WHERE user_id = ?", (name, user_id))
            self.db.commit()
            return 'user_ex'
            
    def get_users(self):
        users = self.cursor.execute('SELECT * FROM users').fetchall()
        return users
    
    def add_anime(self, name, link, series):
        anime_ex = self.cursor.execute("SELECT * FROM anime WHERE name = ?", (name,)).fetchone()
        if not anime_ex:
            self.cursor.execute("INSERT INTO anime (name, link, series) VALUES (?, ?, ?)", (name, link, series))
            self.db.commit()
            
    def update_anime(self, name, option, describtion, img_url):
        anime_ex = self.cursor.execute("SELECT * FROM anime WHERE name = ?", (name,))

        self.cursor.execute("UPDATE anime SET name = ?, options = ?, description = ?, img_url = ? WHERE name = ?", (name, option, describtion, img_url, name))
        self.db.commit()
            
    def all_anime(self):
        anime = self.cursor.execute("SELECT * FROM anime").fetchall()
        return anime
    
    def add_to_viewed(self, name, link, series, option, describtion, img_url):
        anime_ex = self.cursor.execute("SELECT * FROM viewed WHERE name = ?", (name,)).fetchone()
        if not anime_ex:
            self.cursor.execute("INSERT INTO anime (name, link, series, option, describtion, img_url) VALUES (?, ?, ?, ?, ?, ?)", (name, link, series, option, describtion, img_url))
            self.db.commit()
            
    def all_viewed(self):
        viewed = self.cursor.execute("SELECT * FROM viewed").fetchall()
        return viewed
    
    def add_to_favorite(self, name, link, series, option, describtion, img_url):
        anime_ex = self.cursor.execute("SELECT * FROM favorite WHERE name = ?", (name,)).fetchone()
        if not anime_ex:
            self.cursor.execute("INSERT INTO anime (name, link, series, option, describtion, img_url) VALUES (?, ?, ?, ?, ?, ?)", (name, link, series, option, describtion, img_url))
            self.db.commit()
            
    def all_favorite(self):
        viewed = self.cursor.execute("SELECT * FROM favorites").fetchall()
        return viewed
    
    def get_links(self):
        links = self.cursor.execute("SELECT * FROM anime WHERE options IS NULL").fetchall()
        print(links)
        return links
    
    def delete_null(self):
        self.cursor.execute("DELETE FROM anime WHERE options IS NULL")
        self.db.commit()
    