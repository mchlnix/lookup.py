import gtk

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


class ResultBox(gtk.VBox):
    def __init__(self, file_path):
        super(self.__class__, self).__init__()
	self.file_path = file_path

        self.content = FileContentProvider(file_path)

        self.content.open()

    def add_entry(self, entry):
        self.content.add(entry)

    def save_content(self):
        self.content.save()

    def update(self, string):
        self.destroy_children()

        if not string:
            return

        lst = self.content.get_all(string)

        for item in lst:
            label = gtk.Label()
            label.set_justify(gtk.JUSTIFY_LEFT)
            label.set_use_markup(True)
            label.set_markup(self.content.highlight(item, string))

            lalign = gtk.Alignment(0,0,0,0)
            lalign.set_padding(0,0,5,5)

            lalign.add(label)

            self.add(lalign)

    def destroy_children(self):
        for child in self.get_children():
            child.destroy()
