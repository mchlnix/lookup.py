from IContentProvider import IContentProvider

class FileContentProvider(IContentProvider):
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = []

    def open(self):
        try:
            with open(self.file_path, "r+") as f:
                for line in f.readlines():
                    if line.strip():
                        self.content.append(line.strip())
        except IOError as e:
            print e

    def add(self, item):
        if not item in self.content:
            self.content.append(item)

    def sync(self):
        self.open()

    def save(self):
        with open(self.file_path, "w") as f:
            f.write("\n".join(self.content))

    def close(self):
        self.save()

    def get_all(self, query=""):
        if query:
            return [ item for item in self.content if item.lower().find(query.lower()) >= 0 ]
        else:
            return self.content

    def highlight(self, item, query):
        index = item.lower().find(query.lower())
        end = index+len(query)

        if index >=0:
            return item[0:index] + "<b>" + item[index:end] + "</b>" + item[end:]
        else:
            return item