class Database:
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key, None)

    def delete(self, key):
        if key in self.data:
            del self.data[key]

    def exists(self, key):
        return key in self.data

    def keys(self):
        return list(self.data.keys())

    def clear(self):
        self.data.clear()

    def set_multiple(self, items):
        for key, value in items.items():
            self.set(key, value)

    def get_multiple(self, keys):
        return {key: self.get(key) for key in keys}