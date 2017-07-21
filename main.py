# coding: utf-8

import Tkinter
import keybinder
import gtk
import random

keystr = "<Ctrl>I"
file_path = "/tmp/python_blub"

class ResultBox(gtk.VBox):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.last_query = ""
        self.last_slice = []

        self.load_content()

    def load_content(self):
        self.content = []
        with open(file_path, "r") as f:
            for line in f.readlines():
                if line.strip():
                    self.content.append(line.strip())

    def add_entry(self, entry):
        self.content.append(entry)

    def save_content(self):
        with open(file_path, "w") as f:
            f.write("\n".join(self.content))

    def update(self, string):
        self.destroy_children()

        if not string:
            self.last_query = ""
            return

        if self.last_query and string.find(self.last_query) == 0:
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


wind = gtk.Window()
wind.set_decorated(False)

vbox = gtk.VBox()

wind.add(vbox)

query_box = gtk.Entry()

entries = ResultBox()

vbox.add(query_box)
vbox.add(entries)

def ctrl_enter(widget, event):
    if gtk.gdk.keyval_name(event.keyval) == "Return":
        if event.state & gtk.gdk.CONTROL_MASK:
            entries.add_entry(widget.get_text())
        else:
            print "Normal Return"

query_box.connect("key-press-event", ctrl_enter)

def callback():
    if wind.get_visible():
        wind.hide()
    else:
        wind.show_all()

def on_change(widget):
    entries.update(widget.get_text())

    wind.resize(2,2)

    wind.show_all()



query_box.connect("changed", on_change)
    
keybinder.bind(keystr, callback)

wind.show_all()

try:
    gtk.main()
except KeyboardInterrupt:
    entries.save_content()


