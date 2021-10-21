'''
Funciones gestion clientes
'''

import var
from window import *
import events

class Clientes():
    def validarDNI():
        try:
            dni = var.ui.txtDNI.text()
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE' #letras dni
            dig_ext = 'XYZ'                    #digitos extrangeros
            reemp_dig_ext = { 'X': '0', 'Y': '1', 'Z': '2' }
            numeros = '1234567890'
            dni = dni.upper() #conver la letra a mayúsculas
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) %23] == dig_control:
                    var.ui.lblValidoDni.setStyleSheet('QLabel {color: green;}')
                    var.ui.lblValidoDni.setText('V')
                else:
                    var.ui.lblValidoDni.setStyleSheet('QLabel {color: red;}')
                    var.ui.txtDNI.setStyleSheet('QLineEdit {background-color: pink;}')
                    var.ui.lblValidoDni.setText('X')
        except Exception as error:
            print('Error en módulo validar el dni')

    def SelSexo(self):
        try:
            if var.ui.rbtFem.isChecked():
                print('Marcado femenino')
            if var.ui.rbtHom.isChecked():
                print('Marcado masculino')
        except Exception as error:
            print('Error en módulo seleccionar sexo:', error)

    def selPago(self):
        try:
            if var.ui.chkEfectivo.isChecked():
                print('Has seleccionado efectivo')
            if var.ui.chkTarjeta.isChecked():
                print('Has seleccionado Tarjeta')
            if var.ui.chkCargoCuenta.isChecked():
                print('Has seleccionado cargar en cuenta')
            if var.ui.chkTransfe.isChecked():
                print('Has seleccionado transferencia')

        except Exception as error:
            print('Error en módulo seleccionar forma de pago', error)

    def cargaProv(self):
        try:
            var.ui.cmbPro.clear()
            prov = ['', 'A Coruña', 'Lugo', 'Ourense', 'Pontevedra', 'Vigo']
            for i in prov:
                var.ui.cmbPro.addItem(i)
        except Exception as error:
            print('Error en módulo cargar provincias', error)

    def selProv(prov):
        try:
            print('Has seleccionado la provincia de', prov)
            return prov
        except Exception as error:
            print('Error selección provincia', error)

    def cargarFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtAltaCli.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error cargar fecha en txtFecha', error)

    #Función que pone la primera letra del nombre, apellido en mayuscula
    def mayustxt():
        try:
            apellido = var.ui.txtApel.text()
            nombre = var.ui.txtNome.text()
            direccion = var.ui.txtDir.text()
            var.ui.txtApel.setText(str(apellido.title()))
            var.ui.txtNome.setText(str(nombre.title()))
            var.ui.txtDir.setText(str(direccion.title()))
        except Exception as error:
            print('Error en módulo mayuscula txt')

    def limpiaFormCli(self):
        try:
            cajas = [var.ui.txtDNI, var.ui.txtApel, var.ui.txtNome, var.ui.txtAltaCli, var.ui.txtDir]
            for i in cajas:
                i.setText('')
            var.ui.rbtGroupSex.setExclusive(False)
            var.ui.rbtFem.setChecked(False)
            var.ui.rbtHom.setChecked(False)
            var.ui.rbtGroupSex.setExclusive(True)
            var.ui.chkTarjeta.setChecked(False)
            var.ui.chkTransfe.setChecked(False)
            var.ui.chkEfectivo.setChecked(False)
            var.ui.chkCargoCuenta.setChecked(False)
            var.ui.cmbPro.setCurrentIndex(0)
            var.ui.cmbMuni.setCurrentIndex(0)
        except Exception as error:
            print('Error en limpiar formulario clientes', error)



    def cargaCli(self):
        try:
            fila = var.ui.tabClientes.selectedItems()
            datos = [var.ui.txtDNI, var.ui.txtApel, var.ui.txtNome, var.ui.txtAltaCli]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])
                if i == 5:
                    pass
        except Exception as Error:
            print('Error en guardar clientes ', Error)


    def guardaCli(self):
        try:
            if (var.ui.lblValidoDni.text() == 'V'):
                # Preparamos el registro
                newcli = []
                tabcli = []
                client = [var.ui.txtDNI, var.ui.txtApel, var.ui.txtNome, var.ui.txtAltaCli]
                pagos = []
                # Codigo para cargar en tabla
                for i in client:
                    newcli.append(i.text())
                if var.ui.chkCargoCuenta.isChecked():
                    pagos.append('Cargo Cuenta')
                if var.ui.chkTransfe.isChecked():
                    pagos.append('Transeferencia')
                if var.ui.chkTarjeta.isChecked():
                    pagos.append('Tarjeta')
                if var.ui.chkEfectivo.isChecked():
                    pagos.append('Efectivos')

                pagos = set(pagos)
                tabcli.append(', '.join(pagos))
                row = 0
                column = 0
                var.ui.tabClientes.insertRow(row)
                for campo in newcli:
                    cell = QtWidgets.QTableWidgetItem(campo)
                    var.ui.tabClientes.setItem(row, column, cell)
                    column += 1
            else:
                events.Eventos.errorDni(self)

        except Exception as error:
            print('Error en guardar clientes', error)

