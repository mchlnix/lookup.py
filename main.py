# coding: utf-8

import gtk
from App import App

app = App()
    
try:
    app.start()
except KeyboardInterrupt:
    app.exit()
