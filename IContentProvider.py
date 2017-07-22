class IContentProvider:
    def __init__(self):
        pass

    def open(self):
        raise NotImplementedError

    def add(self, item):
        raise NotImplementedError

    def sync(self):
        raise NotImplementedError

    def save(self):
        raise NotImplementedError

    def remove(self, item):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def get_all(self, query):
        raise NotImplementedError

    def highlight(self, item, query):
        raise NotImplementedError