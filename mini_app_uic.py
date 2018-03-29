#!/usr/bin/env python3
# mini_app_uic.py

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

def slot():
	print('Hello Qt!')

app = QApplication([])
ui = uic.loadUi('gui.ui')

ui.button.clicked.connect(slot)
ui.button.clicked.connect(app.quit)

ui.show()

app.exec_()

