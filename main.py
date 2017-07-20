# coding: utf-8

import Tkinter
import keybinder
import gtk
import random

keystr = "<Ctrl>I"

wind = gtk.Window()
wind.set_decorated(False)

vbox = gtk.VBox()

wind.add(vbox)

entry = gtk.Entry()

found_entries = gtk.VBox()

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

    for child in found_entries.get_children():
        child.destroy()

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
