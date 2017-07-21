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
            return

        lst = [ item for item in self.content if item.find(string) >= 0 ]

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

    def destroy_children(self):
        for child in self.get_children():
            child.destroy()


wind = gtk.Window()
wind.set_decorated(False)

vbox = gtk.VBox()

wind.add(vbox)

entry = gtk.Entry()

found_entries = ResultBox()

vbox.add(entry)
vbox.add(found_entries)

entries = []

for i in range(10):
    entries.append(str(random.random()))
    found_entries.add(gtk.Label(entries[i]))

def callback():
    if wind.get_visible():
        wind.hide()
    else:
        wind.show_all()

def on_change(widget):
    found_entries.update(widget.get_text())

    wind.resize(2,2)

    for entry in entries:
        index = entry.find(widget.get_text())
        if index >= 0:
            end = index+len(widget.get_text())
            label = gtk.Label()
            label.set_use_markup(True)
            label.set_markup(entry[0:index] + "<b>" + entry[index:end] + "</b>" + entry[end:-1])
            found_entries.add(label)
            continue


    wind.show_all()



entry.connect("changed", on_change)
    
keybinder.bind(keystr, callback)

wind.show_all()

gtk.main()
