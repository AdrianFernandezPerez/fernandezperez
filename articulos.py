'''
Funciones gestion articulos
'''
import locale

import conexion
import var
from window import *
locale.setlocale(locale.LC_ALL, '')

class Articulos():

    # Función que pone la primera letra del nombre, apellido en mayuscula
    def mayustxt():
        try:
            nombre = var.ui.txtNomeArticulo.text()
            var.ui.txtNomeArticulo.setText(str(nombre.title()))
        except Exception as error:
            print('Error en módulo mayuscula txt')

    # Función para limpiar el formulario de articulos
    def limpiaFormArticulo(self):
        try:
            cajas = [var.ui.txtIdArticulo, var.ui.txtNomeArticulo, var.ui.txtPrecioArticulo]
            for i in cajas:
                i.setText('')
        except Exception as error:
            print('Error en limpiar formulario articulos', error)

    '''
    Metodo para guardar el articulo
    '''
    def guardaArticulo(self):
        try:
            # preparamos el registro
            newart = []
            articulo = [var.ui.txtNomeArticulo, var.ui.txtPrecioArticulo]  # para base de datos
            tabart = []  # para tablewidget
            art = [var.ui.txtNomeArticulo, var.ui.txtPrecioArticulo]
            # código para cargar en la tabla el cliente y la forma de pago
            for i in articulo:
                newart.append(i.text())
            for i in art:
                tabart.append(i.text())
            # cargamos la tabla
            if (var.ui.txtNomeArticulo.text() !=''):
                conexion.Conexion.altaArticulo(newart)
                conexion.Conexion.cargaTabArt(self)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('Articulo no válido, introduce un nombre')
                msg.exec()

            # código para grabar en la base de datos
        except Exception as error:
            print('Error en guardar articulos', error)

    '''
    Metodo para cargar todos los datos del articulos seleccionado en la tabla
    '''
    def cargaArticulo(self):
        try:
            fila = var.ui.tabArticulos.selectedItems()
            datos = [var.ui.txtIdArticulo, var.ui.txtNomeArticulo, var.ui.txtPrecioArticulo]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])
        except Exception as Error:
            print('Error en cargar un articulo ', Error)

    '''
    Metodo para pasar el id al metodo que da de baja un articulo
    '''
    def bajaArticulo(self):
        try:
            if var.ui.txtIdArticulo.text() != '':
                id = var.ui.txtIdArticulo.text()
                conexion.Conexion.bajaArticulo(id)
                conexion.Conexion.cargaTabArt(self)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('Articulo no seleccionado para eliminar')
                msg.exec()

        except Exception as error:
            print('Problemas en baja cliente', error)

    '''
    Metodo para capturar los datos del articulo a modificar y pasarlo al metodo que lo modifica
    '''
    def modifArticulo(self):
        try:
            if var.ui.txtIdArticulo.text() != '':
                modArticulo = []
                articulo = [var.ui.txtIdArticulo, var.ui.txtNomeArticulo, var.ui.txtPrecioArticulo]
                for i in articulo:
                    modArticulo.append(i.text())
                conexion.Conexion.modifArticulo(modArticulo)
                conexion.Conexion.cargaTabArt(self)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('Selecciona un articulo a modificar')
                msg.exec()

        except Exception as error:
            print('Problemas en actualizar el articulo', error)

    def buscArticulo(self):
        try:
            nombre = var.ui.txtNomeArticulo.text()
            if nombre != "":
                conexion.Conexion.buscarArticulo(nombre)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Introduce un nombre')
                msg.exec()
        except Exception as error:
            print('Problemas en buscar un articulo en articulos.py', error)