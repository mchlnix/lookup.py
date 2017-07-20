# coding: utf-8

import Tkinter
import keybinder
import gtk

keystr = "<Ctrl>A"

wind = gtk.Window()
butt = gtk.Button("Hide")

wind.add(butt)

butt.show()

def onclick(event):
    wind.hide()
    
butt.connect("clicked", onclick)

def callback( key):
    if wind.get_visible():
        wind.hide()
    else:
        wind.show()
    
keybinder.bind(keystr, callback, "Bla")

gtk.main()
