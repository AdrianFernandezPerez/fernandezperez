# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowordenar.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ordenar(object):
    def setupUi(self, Ordenar):
        Ordenar.setObjectName("Ordenar")
        Ordenar.resize(360, 200)
        Ordenar.setModal(True)
        self.lblaviso = QtWidgets.QLabel(Ordenar)
        self.lblaviso.setGeometry(QtCore.QRect(100, 10, 151, 61))
        self.lblaviso.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.lblaviso.setObjectName("lblaviso")
        self.btnAceptar = QtWidgets.QPushButton(Ordenar)
        self.btnAceptar.setGeometry(QtCore.QRect(130, 150, 81, 23))
        self.btnAceptar.setObjectName("btnAceptar")
        self.cmbCampo = QtWidgets.QComboBox(Ordenar)
        self.cmbCampo.setGeometry(QtCore.QRect(140, 90, 69, 22))
        self.cmbCampo.setObjectName("cmbCampo")

        self.retranslateUi(Ordenar)
        QtCore.QMetaObject.connectSlotsByName(Ordenar)

    def retranslateUi(self, Ordenar):
        _translate = QtCore.QCoreApplication.translate
        Ordenar.setWindowTitle(_translate("Ordenar", "Dialog"))
        self.lblaviso.setText(_translate("Ordenar", "Ordenar por"))
        self.btnAceptar.setText(_translate("Ordenar", "Aceptar"))