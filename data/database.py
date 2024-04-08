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
                orig_name TEXT,
                jutsu_link TEXT,
                series TEXT,
                description TEXT,
                img_url TEXT, 
                year INTEGER,
                genre TEXT,
                ratting TEXT,
                animego_link TEXT,
                support TEXT
                )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS viewed (
                a_id TEXT,
                user_id TEXT
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS favorite (
                a_id TEXT,
                user_id TEXT
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS filtr (
                genres TEXT,
                user_id INTEGER
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS todays_anime (
                text TEXT,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
            self.cursor.execute("INSERT INTO anime (name, jutsu_link, series) VALUES (?, ?, ?)", (name, link, series))
            self.db.commit()
        else:
            self.cursor.execute("UPDATE anime SET jutsu_link = ?, series = ? WHERE name = ?", (link, series, name))
            self.db.commit()
            
    def update_anime(self, name,orig_name, year, genre, describtion, img_url):
        anime_ex = self.cursor.execute("SELECT * FROM anime WHERE name = ?", (name,))

        self.cursor.execute("UPDATE anime SET name = ?, orig_name = ?, genre = ?, year = ?, description = ?, img_url = ? WHERE name = ?", (name, orig_name, genre, year, describtion, img_url, name))
        self.db.commit()
            
    def all_anime(self):
        animes = self.cursor.execute("SELECT * FROM anime").fetchall()
        return animes
    
    def add_to_viewed(self, a_id, user_id):
        anime_ex = self.cursor.execute("SELECT * FROM viewed WHERE a_id = ? AND user_id = ?", (a_id, user_id)).fetchone()
        if anime_ex:  
            pass
        else:  
            self.cursor.execute("INSERT INTO viewed (a_id, user_id) VALUES (?, ?)", (a_id, user_id))
            self.db.commit()
            
    def all_viewed(self, user_id):
        viewed = self.cursor.execute("SELECT * FROM viewed WHERE user_id = ?", (user_id,)).fetchall()
        return viewed
    
    def add_to_favorite(self, a_id, user_id):
        anime_ex = self.cursor.execute("SELECT * FROM favorites WHERE a_id = ? AND user_id = ?", (a_id, user_id)).fetchone()
        if anime_ex:  
            pass
        else:  
            self.cursor.execute("INSERT INTO favorites (a_id, user_id) VALUES (?, ?)", (a_id, user_id))
            self.db.commit()
            
    def all_favorite(self, user_id):
        favorite = self.cursor.execute("SELECT * FROM favorites WHERE user_id = ?", (user_id,)).fetchall()
        return favorite
    
    def anime_from_id(self, a_id):
        anime = self.cursor.execute("SELECT * FROM anime WHERE id = ?", (a_id,)).fetchone()
        return anime
    
    def delete_favorite(self, a_id, user_id):
        self.cursor.execute("DELETE FROM favorites WHERE a_id = ? AND user_id = ?", (a_id, user_id))
        self.db.commit()
        
    def delete_viewed(self, a_id, user_id):
        self.cursor.execute("DELETE FROM viewed WHERE a_id = ? AND user_id = ?", (a_id, user_id))
        self.db.commit()
            
    def get_links(self):
        links = self.cursor.execute("SELECT jutsu_link FROM anime WHERE genre IS NULL").fetchall()
        return links
    
    def delete_null(self):
        self.cursor.execute("DELETE FROM anime WHERE options IS NULL")
        self.db.commit()
        
    def is_admin(self, user_id):
        admin = self.cursor.execute("SELECT * FROM admins WHERE user_id = ?", (user_id, )).fetchone()
        return admin 
    
    def is_viewed(self, a_id, user_id):
        is_viewed = self.cursor.execute('SELECT * FROM viewed WHERE a_id = ? AND user_id = ?', (a_id, user_id)).fetchone()
        return is_viewed
    
    def new_admin(self, name, user_id):
        user_exists = self.cursor.execute('SELECT * FROM admins WHERE user_id = ?', (user_id,)).fetchone()
        if not user_exists:
            self.cursor.execute('INSERT INTO admins (user_id, name) VALUES (?, ?)', (user_id, name))
            self.db.commit()
        else:
            self.cursor.execute("UPDATE admins SET name = ? WHERE user_id = ?", (name, user_id))
            self.db.commit()
            return 'user_ex'
    
    def add_animego(self, name, desc, ratting, year, orig_name, genre, link, img_link):
        anime = self.cursor.execute("SELECT * FROM anime WHERE name = ? AND year = ?", (name, year)).fetchone()
        print(anime)
        if not anime:
            self.cursor.execute("INSERT INTO anime (name, orig_name, description, img_url, year, genre, ratting, animego_link) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (name, orig_name, desc, img_link, year, genre, ratting, link))
            self.db.commit()
        else:
            self.cursor.execute("UPDATE anime SET name = ?, orig_name = ?, year = ?, ratting = ?, genre = ?, animego_link = ?, img_url = ?  WHERE name = ?", (name, orig_name, year, ratting, genre, link, img_link, name))
            
    def set_support(self):
        animes = self.cursor.execute("SELECT * FROM anime WHERE support IS NULL").fetchall()
        print(animes)
        for anime in animes:
            self.cursor.execute("UPDATE anime SET support = ? WHERE name = ?", ('multi', anime[1]))
            self.db.commit()
            
            print(anime)
            
    def get_genres(self, user_id):
        genres = self.cursor.execute("SELECT genres FROM filtr WHERE user_id = ?", (user_id, )).fetchall()
        return genres
    
    def set_genres(self, a_genre, user_id):
        f_genres = self.cursor.execute("SELECT genres FROM filtr WHERE user_id = ?", (user_id,)).fetchone()
        genre_ex = self.cursor.execute("SELECT * FROM filtr WHERE genres = ? AND user_id = ?", (a_genre, user_id)).fetchone()

        if f_genres:
            if genre_ex:
                self.cursor.execute("DELETE FROM filtr WHERE genres = ?", (a_genre, ))
            else:
                self.cursor.execute("INSERT INTO filtr (genres, user_id) VALUES (?, ?)", (a_genre, user_id))           
                #self.cursor.execute("UPDATE filtr SET genres = ? WHERE user_id = ?", (a_genre, user_id))
        else:
            self.cursor.execute("INSERT INTO filtr (genres, user_id) VALUES (?, ?)", (a_genre, user_id))
        
        self.db.commit()
         
        genres = self.cursor.execute("SELECT genres FROM filtr WHERE user_id = ?", (user_id, )).fetchall()
        return genres   
        
    def todays_anime(self):
        todays_anime = self.cursor.execute("SELECT text FROM todays_anime").fetchall()
        return todays_anime
    
    
    