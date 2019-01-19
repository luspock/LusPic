# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Client.ui',
# licensing of 'Client.ui' applies.
#
# Created: Thu Jan 17 21:38:18 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(611, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pteFilename = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pteFilename.setGeometry(QtCore.QRect(80, 10, 351, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pteFilename.sizePolicy().hasHeightForWidth())
        self.pteFilename.setSizePolicy(sizePolicy)
        self.pteFilename.setObjectName("pteFilename")
        self.ptePublicLink = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ptePublicLink.setGeometry(QtCore.QRect(90, 470, 361, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ptePublicLink.sizePolicy().hasHeightForWidth())
        self.ptePublicLink.setSizePolicy(sizePolicy)
        self.ptePublicLink.setObjectName("ptePublicLink")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 480, 76, 19))
        self.label_2.setObjectName("label_2")
        self.btnCopy = QtWidgets.QPushButton(self.centralwidget)
        self.btnCopy.setGeometry(QtCore.QRect(460, 480, 136, 27))
        self.btnCopy.setObjectName("btnCopy")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 80, 591, 381))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 63, 19))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(440, 20, 158, 29))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSelect = QtWidgets.QPushButton(self.widget)
        self.btnSelect.setObjectName("btnSelect")
        self.horizontalLayout.addWidget(self.btnSelect)
        self.btnUpload = QtWidgets.QPushButton(self.widget)
        self.btnUpload.setObjectName("btnUpload")
        self.horizontalLayout.addWidget(self.btnUpload)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 611, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Public Link", None, -1))
        self.btnCopy.setText(QtWidgets.QApplication.translate("MainWindow", "Copy to Clipboard", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Filename", None, -1))
        self.btnSelect.setText(QtWidgets.QApplication.translate("MainWindow", "Select", None, -1))
        self.btnUpload.setText(QtWidgets.QApplication.translate("MainWindow", "Upload", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

