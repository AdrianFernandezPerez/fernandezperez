'''

Archivo de eventos generales

'''
import os.path
import shutil
import sys
import zipfile

import xlrd as xlrd

import conexion
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets, QtPrintSupport
from datetime import date, datetime
import var


class Eventos():

    '''
    Metodo para salir del programa
    '''
    def Salir(self):
        try:
            var.dlgaviso.show()
            if var.dlgaviso.exec():
                sys.exit()
            else:
                var.dlgaviso.hide()
        except Exception() as error:
            print('Error en módulo salir', error)

    '''
    Metodo para abrir el calendario
    '''
    def abrircal(self):
        try:
            var.dlgcalendar.show()
        except Exception() as error:
            print('Error al abrir el calendario', error)

    '''
    Metodo para abrir el calendario de facturas
    '''
    def abrircalFac(self):
        try:
            var.dlgcalendarFac.show()
        except Exception() as error:
            print('Error al abrir el calendario', error)

    '''
    Metodo para redimensionar la tabla clientes
    '''
    def resizeTablaCli(self):
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(4):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        except Exception as error:
            print("Error al redimensionar la tabla", error)

    '''
    Metodo el cual muestra un error cuando un dni es erroneo
    '''
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

    '''
    Metodo para abrir el dialogo buscador
    '''
    def Abrir(self):
        try:
            var.dlgabrir.show()
        except Exception as error:
            print('Error al abrir cuadro dialogo', error)

    '''
    Metodo para crear backups
    '''
    def crearBackup(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + '_backup.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar copia', var.copia, '.zip',
                                                                options=option)
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

    '''
    Metodo para restaurar backups
    '''
    def restaurarBackup(self):
        try:

            option = QtWidgets.QFileDialog.Options()
            filename = var.dlgabrir.getOpenFileName(None, 'Restaurar Copia de Seguridade', '', '*.zip;;ALL')

            if var.dlgaviso.Accepted and filename != '':
                file = filename[0]
                print(file)
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
            conexion.Conexion.db_connect(var.filedb)
            conexion.Conexion.cargaTabCli(self)
            # conexion.Conexion.mostrarProducts(self)
            # conexion.Conexion.mostrarFacturas(self)
            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText('Copia de Seguridad Creada')
            msg.exec()

        except Exception as error:
            print('Error al restaurar backup', error)

    '''
    Metodo para abrir la ventana de imprimir 
    '''
    def imprimir(self):
        try:
            printDialog = QtPrintSupport.QPrintDialog()
            if printDialog.exec_():
                printDialog.show()
        except Exception as error:
            print('Error al abrir ventana impresora', error)

    '''
    Metodo para abrir el explorador
    '''
    def AbrirDir(self):
        try:
            var.dlgabrir.show()
        except Exception as error:
            print('Error abrir explorador: %s ' % str(error))

    '''
    Metodo para exportar datos 
    '''
    def ExportarDatos(self):
        try:
            conexion.Conexion.exportExcel(self)
            try:
                msgBox = QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setText("Datos exportados con éxito.")
                msgBox.setWindowTitle("Operación completada")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
            except Exception as error:
                print('Error en mensaje generado exportar datos ', error)
        except Exception as error:
            print('Error en evento exportar datos ', error)

    '''
    Metodo para importar a excel
    '''
    def ImportarExcel(self):
        try:
            newcli = []
            contador = 0
            option = QtWidgets.QFileDialog.Options()
            ruta_excel = var.dlgabrir.getOpenFileName(None, 'Importar Excel', '', '*.xls', options=option)
            if var.dlgabrir.Accepted and ruta_excel != '':
                fichero = ruta_excel[0]
            workbook = xlrd.open_workbook(fichero)
            hoja = workbook.sheet_by_index(0)
            while contador < hoja.nrows:
                for i in range(6):
                    # if i==1:
                    #     newcli.append((str)(date.today()))
                    # if i==5:
                    #     newcli.append('')
                    newcli.append(hoja.cell_value(contador + 1, i))
                # newcli.append('Efectivo')
                conexion.Conexion.altaCli2(newcli)
                conexion.Conexion.cargarTabCli(newcli)
                newcli.clear()
                contador = contador + 1
        except Exception as error:
            print('Error al importar ', error)

    '''
    Metodo para redimensionar la tabla articulos
    '''
    def resizeTablaArticulos(self):
        try:
            header = var.ui.tabArticulos.horizontalHeader()
            for i in range(3):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        except Exception as error:
            print("Error al redimensionar la tabla articulos", error)

    def resizeTablaProv(self):
        try:
            header = var.ui.tabProveedores.horizontalHeader()
            for i in range(3):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 2:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeToContents)
        except Exception as error:
            print('Error al redimensionar la tabla proveedores', error)

    def cargarComboOrdenar(self):
        try:
            lstSeccion = ['','Nombre', 'Pago']
            var.dlgordenar.cmbCampo.addItems(lstSeccion)
        except Exception as error:
            print('Problemas en añadir los campos al combo de pagos', error)

    def cargarComboTipo(self):
        try:
            lstSeccion = ['','Pdf', 'Excel']
            var.dlgordenar.cmbTipo.addItems(lstSeccion)
        except Exception as error:
            print('Problemas en añadir los campos al combo de tipos', error)

    def selTipo(self):
        try:

            if var.dlgordenar.rbtPdf.isChecked():
                print("Pdf seleccionado")
            if var.dlgordenar.rbtExcel.isChecked():
                print("Excel seleccionado")
        except Exception as error:
            print('Error al obtener el tipo: ', error)


