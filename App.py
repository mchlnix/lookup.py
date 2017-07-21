import gtk
import keybinder
from ResultBox import ResultBox

keystr = "<Ctrl>I"
file_path = "/tmp/python_blub"

class App:
    def __init__(self):
        self.setup()

    def setup(self):
        self.wind = gtk.Window()
        self.wind.set_decorated(False)
        self.wind.connect("key-press-event", self.escape_listener)

        vbox = gtk.VBox()

        self.wind.add(vbox)

        self.query_box = gtk.Entry()
        vbox.add(self.query_box)

        self.query_box.connect("key-press-event", self.ctrl_enter_listener)
        self.query_box.connect("changed", self.query_input_listener)

        self.entries = ResultBox(file_path)
        vbox.add(self.entries)

        keybinder.bind(keystr, self.keybinder_callback)

        self.wind.show_all()

    def exit(self):
        self.entries.save_content()

    def ctrl_enter_listener(self, widget, event):
        if gtk.gdk.keyval_name(event.keyval) == "Return":
            if event.state & gtk.gdk.CONTROL_MASK:
                self.entries.add_entry(widget.get_text())

    def escape_listener(self, widget, event):
        if gtk.gdk.keyval_name(event.keyval) == "Escape":
            if event.state & gtk.gdk.CONTROL_MASK:
                print "Close Application"
            else:
                print "Hide Application"
        else:
            print gtk.gdk.keyval_name(event.keyval)

    def keybinder_callback(self):
        if self.wind.get_visible():
            self.wind.hide()
        else:
            self.wind.show_all()

    def query_input_listener(self, widget):
        self.entries.update(widget.get_text())

        self.wind.resize(1,1)

        self.wind.show_all()
