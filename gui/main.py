#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:18:47 2019

@author: dh
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QDockWidget, QListWidget, QTextEdit
from PyQt5.QtGui import QIcon

#%%
class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(953, 692)

        self.slider = QtWidgets.QWidget(Main)
        self.slider.setGeometry(QtCore.QRect(0, 640, 951, 51))
        self.slider.setObjectName("slider")

        self.horizontalSlider = QtWidgets.QSlider(self.slider)
        self.horizontalSlider.setGeometry(QtCore.QRect(40, 10, 801, 31))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.label = QtWidgets.QLabel(self.slider)
        self.label.setGeometry(QtCore.QRect(853, 10, 91, 31))
        self.label.setObjectName("label")

        self.dockWidget = QtWidgets.QDockWidget(Main)
        self.dockWidget.setGeometry(QtCore.QRect(80, 20, 751, 501))
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Main"))
        self.label.setText(_translate("Main", "TextLabel"))

#%%


class MyMainWindow(QMainWindow):


    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        APP_WIDTH   = 800
        APP_HEIGHT  = 600

        self.setGeometry(300, 300, APP_WIDTH, APP_HEIGHT)
        self.setWindowTitle('Main')

        self.add_slider()

    def add_slider(self):
        self._SLIDER_MIN_VAL = 1
        self._SLIDER_MAX_VAL = 1800

        SLIDER_HEIGHT = 50

        x = 0
        y = self.height() - SLIDER_HEIGHT
        width = self.width()
        height = SLIDER_HEIGHT

        self.slider_pane = QtWidgets.QWidget(self)
        self.slider_pane.setGeometry(QtCore.QRect(x, y, width, height))

        x = 40
        y = 10
        MARGIN_LEFT     = 40
        MARGIN_RIGHT    = 100
        MARGIN_TOP      = 0
        MARGIN_BOTTOM   = 0
        width = self.width() - (MARGIN_LEFT + MARGIN_RIGHT)
        height = SLIDER_HEIGHT - (MARGIN_TOP + MARGIN_BOTTOM)

        self.slider = QtWidgets.QSlider(self.slider_pane)
        self.slider.setGeometry(QtCore.QRect(x, y, width, height))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setRange(self._SLIDER_MIN_VAL, self._SLIDER_MAX_VAL)

        x = self.slider_pane.width() - MARGIN_RIGHT
        y = 10
        width = MARGIN_RIGHT
        height = SLIDER_HEIGHT

        self.slider_text = QtWidgets.QLabel(self.slider_pane)
        self.slider_text.setGeometry(QtCore.QRect(x, y, width, height))
        self.update_slider_text(self._SLIDER_MIN_VAL)

        self.slider.valueChanged.connect(self.update_slider_text)

    def update_slider_text(self, value):
        max_val = self._SLIDER_MAX_VAL

        val_str = f'{value:d}'
        max_str = f'{max_val:d}'

        max_len = len(max_str)

        slider_text = f'{val_str: >{max_len}s}/{max_str:s}'

        self.slider_text.setText(slider_text)



#%%

def main():
    app = QApplication(sys.argv)
#    ex = Example()

#    ui = Ui_Main()

#    ui.setupUi(ex)

    self = MyMainWindow()
    self.show()

    sys.exit(app.exec_())




if __name__ == '__main__':
    main()
