import gtk

class ResultBox(gtk.VBox):
    def __init__(self, content_provider):
        super(self.__class__, self).__init__()

        self.content = content_provider

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
