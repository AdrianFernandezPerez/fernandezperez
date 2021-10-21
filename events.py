'''

Archivo de eventos generales

'''

import sys
from window import *
import var
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets

import var


class Eventos():
    def Salir(self):
        try:
            var.dlgaviso.show()
            if var.dlgaviso.exec():
                sys.exit()
            else:
                var.dlgaviso.hide()
        except Exception() as error:
            print('Error en módulo salir', error)

    def abrircal(self):
        try:
            var.dlgcalendar.show()
        except Exception() as error:
            print('Error al abrir el calendario', error)

    def resizeTablaCli(self):
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(4):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        except Exception as error:
            print("Error al redimensionar la tabla", error)

    def errorDni(self):
        try:
            msgBox = QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            msgBox.setText("DNI no válido")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        except Exception as error:
            print('Error en mensaje error DNI', error)