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
            newpro.append(var.ui.cmbPago.currentText())
            if var.ui.rbtRecogidaLocal.isChecked():
                newpro.append('Recogida en local')
            else:
                newpro.append('Transporte del pedido')
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
                var.ui.txtFechaFactura.setText(str(data))
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
            var.ui.cmbPago.setCurrentIndex(0)
            var.ui.rbtRecogidaLocal.setChecked(False)
            var.ui.rbtTransportePedido.setChecked(False)
            var.ui.buttonGroup.setExclusive(True)
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
            var.ui.cmbPago.setCurrentText(str(row2[2]))
            if str(row2[3]) == 'Recogida en local':
                var.ui.rbtRecogidaLocal.setChecked(True)
            elif str(row2[3]) == 'Transporte del pedido':
                var.ui.rbtTransportePedido.setChecked(True)
            form2 = [var.ui.txtCif, var.ui.txtEmail]
            for i, dato in enumerate(form2):
                dato.setText(row2[i])
        except Exception as error:
            print('Error al cargar los datos de un proveedor')



    '''
    Metodo para pasar el dni al metodo que da de baja un proveedor
    '''
    def bajaProv(self):
        try:
            cif = var.ui.txtCif.text()
            txtNomProv = var.ui.txtNomprov.text()
            print(txtNomProv)
            conexion.Conexion.bajaProv(cif, txtNomProv)
            conexion.Conexion.mostrarProvtab(self)

        except Exception as error:
            print('Problemas en baja proveedor', error)

    def limpiaFormProv(self):
        try:
            cajas = [var.ui.txtCif, var.ui.txtFechaprov, var.ui.txtNomprov, var.ui.txtTelefono, var.ui.txtEmail]
            for i in cajas:
                i.setText('')
            var.ui.cmbPago.setCurrentIndex(0)
            var.ui.buttonGroup.setExclusive(False)
            var.ui.rbtRecogidaLocal.setChecked(False)
            var.ui.rbtTransportePedido.setChecked(False)
            var.ui.buttonGroup.setExclusive(True)
        except Exception as error:
            print('Error en limpiar formulario proveedores', error)

    '''
    Metodo para capturar los datos del proveedor a modificar y pasarlo al metodo que lo modifica
    '''
    def modifProv(self):
        try:
            modprov = []
            prov = [var.ui.txtCif, var.ui.txtFechaprov, var.ui.txtNomprov, var.ui.txtTelefono, var.ui.txtEmail]
            for i in prov:
                modprov.append(i.text())
            modprov.append(var.ui.cmbPago.currentText())
            if var.ui.rbtRecogidaLocal.isChecked():
                modprov.append('Recogida en local')
            else:
                modprov.append('Transporte del pedido')
            print(modprov)
            conexion.Conexion.modifProv(modprov)
            conexion.Conexion.mostrarProvtab(self)
        except Exception as error:
            print('Problemas en actualizar el proveedor', error)

    def cargarFormasPagoCombo(self):
        try:
            lstSeccion = ['','Transferencia', 'Cargo de Cuenta', 'Efectivo', 'Tarjeta']
            var.ui.cmbPago.addItems(lstSeccion)
        except Exception as error:
            print('Problemas en añadir los campos al combo de pagos', error)
