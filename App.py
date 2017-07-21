import gtk
import keybinder
import errno
import os
from ResultBox import ResultBox

keystr = "<Ctrl>I"

data_folder = os.path.expanduser("~/.config/lookup.py/")
file_path = data_folder + "/data.txt"

class App:
    def __init__(self):
        # create folder to save data in
        # https://stackoverflow.com/a/600612/4252230
        try:
            os.makedirs(data_folder)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(data_folder):
                pass
            else:
                print("There was a problem while creating the data directory " + data_folder)
                raise

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
                self.entries.refresh()
                self.redraw()

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
        self.wind.resize(1,1)

        self.wind.show_all()
