import conexion
import var
from PyQt5 import QtWidgets, QtCore

class Proveedor():

    def altaprov(self):
        try:
            newpro = []
            newpro.append(str(var.ui.txtCif.text()))
            newpro.append(str(var.ui.txtNomprov.text()))
            newpro.append(str(var.ui.txtFechaprov.text()))
            newpro.append(str(var.ui.txtEmail.text()))
            newpro.append(str(var.ui.txtTelefono.text()))

            conexion.Conexion.altaproveedor(newpro)

        except Exception as error:
            print("error en alta proveedor ", error)

    def calendarpro(self):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print("Abrir calendario ", error)

    def cargarFecha(qDate):
        """

        Carga la fecha elegida en el widget Calendar
        :param qDate:
        :type qDate:

        """
        try:
            data = (str(qDate.day()).zfill(2) + '/' + str(qDate.month()).zfill(2) + '/' + str(qDate.year()))
            if var.ui.tabWidget.currentIndex() == 0:
                var.ui.txtAltaCli.setText(str(data))
            elif var.ui.tabWidget.currentIndex() == 1:
                var.ui.txtFechafac.setText(str(data))
            elif var.ui.tabWidget.currentIndex() == 3:
                var.ui.txtFechaprov.setText(str(data))
            var.dlgcalendar.hide()

        except Exception as error:
            print('Error cargar fecha en txtFecha', error)

    def limpiar(self = None):
        try:
            form = [var.ui.txtCif, var.ui.txtFechaprov, var.ui.txtNomprov, var.ui.txtEmail, var.ui.txtTelefono]
            for dato in form:
                dato.setText('')
        except Exception as error:
            print('Error en limpiar formulario proveedor')

    def cargarProv(self = None):
        try:
            Proveedor.limpiar(self)
            fila = var.ui.tabProveedores.selectedItems()
            form = [var.ui.txtNomprov, var.ui.txtFechaprov, var.ui.txtTelefono]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(form):
                dato.setText(row[i])
            row2 = conexion.Conexion.datosprov(row[0])
            form2 = [var.ui.txtCif, var.ui.txtEmail]
            for i, dato in enumerate(form2):
                dato.setText(row2[i])
        except Exception as error:
            print('Error al cargar los datos de un proveedor')