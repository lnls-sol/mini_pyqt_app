#!/usr/bin/env python3
# mini_app.py

from PyQt5.QtWidgets import QApplication, QPushButton


def slot():
	print('Hello Qt!')

app = QApplication([])
button = QPushButton('Click me')

button.clicked.connect(slot)
button.clicked.connect(app.quit)

button.show()

app.exec_()

