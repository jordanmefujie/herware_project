import json


class FileStorage:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = self._load_data_from_file()

    def _load_data_from_file(self):
        if json.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                self.data = json.load(file)
        else:
            self.data = {}

    def save_to_file(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get_from_file(self, key):
        return self.data.get(key)

    def set_in_file(self, key, value):
        self.data[key] = value
        self.save_to_file()


class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.bookmarks = []


class Bookmark:
    def __init__(self, user_id, title, url):
        self.user_id = user_id
        self.title = title
        self.url = url


def create_user_in_file(file_storage, user):
    file_storage.data['users'][str(user.user_id)] = {
        'name': user.name,
        'email': user.email,
        'bookmarks': user.bookmarks
    }
    file_storage.save_to_file()


def create_bookmark_in_file(file_storage, bookmark):
    user_id = str(bookmark.user_id)
    if user_id in file_storage.data['users']:
        file_storage.data['users'][user_id]['bookmarks'].append({
            'title': bookmark.title,
            'url': bookmark.url
        })
        file_storage.save_to_file()
