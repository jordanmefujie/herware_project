# db_storage.py
import json


class DBStorage:
    def __init__(self, db_file):
        self.db_file = db_file
        self._load_db_from_file()

    def _load_db_from_file(self):
        if json.exists(self.db_file):
            with open(self.db_file, 'r') as file:
                self.database = json.load(file)
        else:
            self.database = {}

    def save_to_db(self):
        with open(self.db_file, 'w') as file:
            json.dump(self.database, file, indent=4)

    def get_from_db(self, key):
        return self.database.get(key)

    def set_in_db(self, key, value):
        self.database[key] = value
        self.save_to_db()


class Bookmark:
    def __init__(self, user_id, title, url):
        self.user_id = user_id
        self.title = title
        self.url = url


class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.bookmarks = []


def create_user_in_db(db, user):
    db['users'][str(user.user_id)] = {
        'name': user.name,
        'email': user.email,
        'bookmarks': user.bookmarks
    }
    db.save_to_db()


def create_bookmark_in_db(db, bookmark):
    user_id = str(bookmark.user_id)
    if user_id in db['users']:
        db['users'][user_id]['bookmarks'].append({
            'title': bookmark.title,
            'url': bookmark.url
        })
        db.save_to_db()
