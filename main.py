# coding: utf-8

import Tkinter
import keybinder
import gtk
import random

from ResultBox import ResultBox

keystr = "<Ctrl>I"
file_path = "/tmp/python_blub"

wind = gtk.Window()
wind.set_decorated(False)

vbox = gtk.VBox()

wind.add(vbox)

query_box = gtk.Entry()

entries = ResultBox(file_path)

vbox.add(query_box)
vbox.add(entries)

def ctrl_enter(widget, event):
    if gtk.gdk.keyval_name(event.keyval) == "Return":
        if event.state & gtk.gdk.CONTROL_MASK:
            entries.add_entry(widget.get_text())
        else:
            print "Normal Return"

query_box.connect("key-press-event", ctrl_enter)

def esc_listener(widget, event):
    if gtk.gdk.keyval_name(event.keyval) == "Escape":
        if event.state & gtk.gdk.CONTROL_MASK:
            print "Close Application"
        else:
            print "Hide Application"
    else:
        print gtk.gdk.keyval_name(event.keyval)

wind.connect("key-press-event", esc_listener)

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


