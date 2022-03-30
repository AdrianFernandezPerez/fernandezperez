import conexion
import var
from PyQt5 import QtWidgets, QtCore

class Facturas():

    '''
    Funcion que busca un cliente por el dni
    '''
    def buscaCli(self):
        try:
            dni = var.ui.txtDni.text().upper()
            var.ui.txtDni.setText(dni)
            registro = conexion.Conexion.buscaClifac(dni)
            if registro:
                nombre = registro[0] + ', ' + registro[1]
                var.ui.txtCliente.setText(nombre)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('No existe el cliente')
                msg.exec()
        except Exception as error:
            print('Error en buscar el cliente', error)

    '''
    Función que muestra los datos de la factura seleccionada en la tabla
    '''
    def cargaFac(self):
        try:
            fila = var.ui.tabFacturas.selectedItems()
            datos = [var.ui.lblNumFac, var.ui.txtFechaFactura]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])
            #aquí cargamos el dni y nombre cliente
            dni = conexion.Conexion.buscaDNIFac(row[0])
            var.ui.txtDni.setText(str(dni))
            registro = conexion.Conexion.buscaClifac(dni)
            if registro:
                nombre = registro[0] + ', ' + registro[1]
                var.ui.txtCliente.setText(nombre)
        except Exception as error:
            print('Error alta en factura', error)

    '''
    Función para pasar los valores de la factura a crear a conexion
    '''
    def facturar(self):
        try:
            registro = [var.ui.txtDni.text(), var.ui.txtFechaFactura.text()]
            print(registro)
            conexion.Conexion.altaFac(registro)
        except Exception as error:
            print('Error al facturar en invoice')


    def cargaLineaVenta(self):
        try:
            index = 0
            var.cmbProducto = QtWidgets.QComboBox()
            var.cmbProducto.setFixedSize(180, 25)
            conexion.Conexion.cargaCmbproducto(var.cmbProducto)
            var.txtCantidad.setFixedSize(70,25)
            var.txtCantidad.setAlignment(QtCore.Qt.AlignCenter)
            var.ui.tabVentas.setRowCount(index+1)
            var.ui.tabVentas.setCellWidget(index, 1, var.cmbProducto)
            var.ui.tabVentas.setCellWidget(index, 3, var.txtCantidad)
        except Exception as error:
            print('Error carga linea venta', self)

    def procesoVenta(self):
        try:
            row = var.ui.tabVentas.currentRow()
            articulo = var.cmbProducto.currentText()
            dato = conexion.Conexion.obtenerCodPrecio(articulo)
            var.ui.tabVentas.item(row,2).setTextAlignment(QtCore.Qt.AlignCenter)
            var.ui.tabVentas.setItem(row, 2, QtWidgets.QTableWidgetItem(str(dato[1])))
        except Exception as error:
            print('Error proceso venta', self)