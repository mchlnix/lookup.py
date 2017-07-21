import gtk

class ResultBox(gtk.VBox):
    def __init__(self, file_path):
        super(self.__class__, self).__init__()
        self.last_query = ""
        self.last_slice = []

	self.file_path = file_path

        self.load_content()

    def load_content(self):
        self.content = []
        with open(self.file_path, "r") as f:
            for line in f.readlines():
                if line.strip():
                    self.content.append(line.strip())

    def add_entry(self, entry):
        if not entry in self.content:
            self.content.append(entry)

    def save_content(self):
        with open(self.file_path, "w") as f:
            f.write("\n".join(self.content))

    def refresh(self):
        self.update(self.last_query, use_cache=False)

    def update(self, string, use_cache=True):
        self.destroy_children()

        if not string:
            self.last_query = ""
            return

        if use_cache and self.last_query and string.find(self.last_query) == 0:
            print("Using " + str(len(self.last_slice)) + " entries")
            content = self.last_slice
        else:
            content = self.content

        self.last_query = string

        lst = [ item for item in content if item.find(string) >= 0 ]

        for item in lst:
            index = item.find(string)
            end = index+len(string)

            label = gtk.Label()
            label.set_justify(gtk.JUSTIFY_LEFT)
            label.set_use_markup(True)
            label.set_markup(item[0:index] + "<b>" + item[index:end] + "</b>" + item[end:])

            lalign = gtk.Alignment(0,0,0,0)
            lalign.set_padding(0,0,5,5)

            lalign.add(label)

            self.add(lalign)

        self.last_slice = lst

    def destroy_children(self):
        for child in self.get_children():
            child.destroy()
