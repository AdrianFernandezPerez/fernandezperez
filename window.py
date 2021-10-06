# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(430, 310, 173, 75))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lblTitulo = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setObjectName("lblTitulo")
        self.gridLayout.addWidget(self.lblTitulo, 0, 0, 1, 2)
        self.btnAceptar = QtWidgets.QPushButton(self.layoutWidget)
        self.btnAceptar.setObjectName("btnAceptar")
        self.gridLayout.addWidget(self.btnAceptar, 2, 0, 1, 1)
        self.btnSalir = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btnSalir.setFont(font)
        self.btnSalir.setObjectName("btnSalir")
        self.gridLayout.addWidget(self.btnSalir, 2, 1, 1, 1)
        self.txtDatos = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtDatos.setObjectName("txtDatos")
        self.gridLayout.addWidget(self.txtDatos, 1, 0, 1, 2)
        self.lblClientes = QtWidgets.QLabel(self.centralwidget)
        self.lblClientes.setGeometry(QtCore.QRect(420, 220, 211, 41))
        self.lblClientes.setStyleSheet("font: 75 italic 18pt \"Noto Sans\";")
        self.lblClientes.setObjectName("lblClientes")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTitulo.setText(_translate("MainWindow", "MI PRIMERA VENTANA"))
        self.btnAceptar.setText(_translate("MainWindow", "Aceptar"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
        self.lblClientes.setText(_translate("MainWindow", "XESTIÓN CLIENTES"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Alt+S"))
