'''

Archivo de eventos generales

'''
import os.path
import shutil
import sys
import zipfile

from window import *
import var
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from datetime import date, datetime
from zipfile import ZipFile
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

    def Abrir(self):
        try:
            var.dlgabrir.show()
        except Exception as error:
            print('Error al abrir cuadro dialogo', error)

    def crearBackup(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha)+ '_backup.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar copia', var.copia, '.zip', options = option)
            if var.dlgabrir.Accepted and filename != '':
                fichzip = zipfile.ZipFile(var.copia, 'w')
                fichzip.write(var.filedb, os.path.basename(var.filedb), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(var.copia), str(directorio))

                msgBox = QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setText("BackUp creado con exito")
                msgBox.setWindowTitle("BackUp")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()

        except Exception as error:
            print('Error al crear un backup', error)


    def restaurarBd(self):
        try:
            var.dlgabrir.show()
            if var.dlgabrir.Accepted:
                with zipfile.ZipFile('C:/Users/a19adrianfp/PycharmProjects/fernandezperez/2021.11.11.13.25.20_backup.zip') as zf:
                    for filename in ['bbdd.sqlite']:
                        try:
                            data = str(zf.read(filename))
                        except KeyError:
                            print('ERROR: Did not find {} in zip file'.format(
                                filename))
                        else:
                            print(filename, ':')
                            print(data)
                        print()


        except Exception as error:
            print('Error al restaurar la base de datos', error)