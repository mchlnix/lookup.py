# coding: utf-8

import gtk
from App import App

app = App()
    
try:
    gtk.main()
except KeyboardInterrupt:
    app.exit()
