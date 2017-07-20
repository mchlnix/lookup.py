# coding: utf-8

import Tkinter
import keybinder
import gtk

keystr = "<Ctrl>I"

wind = gtk.Window()
wind.set_decorated(False)

vbox = gtk.VBox()

wind.add(vbox)

entry = gtk.Entry()

butt = gtk.Button("Hide")

vbox.add(entry)
vbox.add(butt)

def onclick(event):
    wind.hide()
    
butt.connect("clicked", onclick)

def callback():
    if wind.get_visible():
        wind.hide()
    else:
        wind.show_all()
    
keybinder.bind(keystr, callback)

wind.show_all()

gtk.main()
