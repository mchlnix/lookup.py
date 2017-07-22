import gtk
import keybinder
import errno
import os
from ResultBox import ResultBox

DEFAULT_WIDTH = 400

KEY_STRING = "<Ctrl>I"

DATA_DIR = os.path.expanduser("~/.config/lookup.py/")
FILE_PATH = DATA_DIR + "/data.txt"

class App:
    def __init__(self):
        # create folder to save data in
        # https://stackoverflow.com/a/600612/4252230
        try:
            os.makedirs(DATA_DIR)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(DATA_DIR):
                pass
            else:
                print("There was a problem while creating the data directory " + DATA_DIR)
                raise

        self.setup()

    def setup(self):
        self.wind = gtk.Window()
        self.wind.set_decorated(False)
        self.wind.set_default_size(DEFAULT_WIDTH, -1)
        self.wind.connect("key-press-event", self.escape_listener)

        vbox = gtk.VBox()

        self.wind.add(vbox)

        self.query_box = gtk.Entry()
        vbox.add(self.query_box)

        self.query_box.connect("key-press-event", self.ctrl_enter_listener)
        self.query_box.connect("changed", self.query_input_listener)

        self.entries = ResultBox(FILE_PATH)
        vbox.add(self.entries)

        keybinder.bind(KEY_STRING, self.keybinder_callback)

        self.wind.show_all()

    def start(self):
        gtk.main()

    def exit(self):
        self.entries.save_content()
        if gtk.main_level() > 0:
            gtk.main_quit()

    def toggle_visibility(self):
        if self.wind.get_visible():
            self.query_box.set_text("")
            self.wind.hide()
        else:
            self.wind.show_all()

    def ctrl_enter_listener(self, widget, event):
        if gtk.gdk.keyval_name(event.keyval) == "Return":
            if event.state & gtk.gdk.CONTROL_MASK:
                self.entries.add_entry(widget.get_text())

                self.query_input_listener(widget)

    def escape_listener(self, widget, event):
        if gtk.gdk.keyval_name(event.keyval) == "Escape":
            if event.state & gtk.gdk.CONTROL_MASK:
                self.exit()
            else:
                self.toggle_visibility()

    def keybinder_callback(self):
        self.toggle_visibility()

    def query_input_listener(self, widget):
        self.entries.update(widget.get_text())

        self.redraw()

    def redraw(self):
        self.wind.resize(DEFAULT_WIDTH,1)

        self.wind.show_all()
