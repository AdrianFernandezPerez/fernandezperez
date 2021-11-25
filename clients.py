'''
Funciones gestion clientes
'''
import conexion
import var
from window import *
import events

class Clientes():

    '''
    Metodo para la validación del dni
    '''
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
            dni = var.ui.txtDNI.text()
            apellido = var.ui.txtApel.text()
            nombre = var.ui.txtNome.text()
            direccion = var.ui.txtDir.text()
            var.ui.txtApel.setText(str(apellido.title()))
            var.ui.txtNome.setText(str(nombre.title()))
            var.ui.txtDir.setText(str(direccion.title()))
            var.ui.txtDNI.setText(str(dni.title()))
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


    '''
    Metodo para cargar todos los datos del cliente seleccionado en la tabla
    '''
    def cargaCli(self):
        try:
            fila = var.ui.tabClientes.selectedItems()
            datos = [var.ui.txtDNI, var.ui.txtApel, var.ui.txtNome, var.ui.txtAltaCli]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])
            if 'Efectivo' in row[4]:
                var.ui.chkEfectivo.setChecked(True)
            if 'Tranferencia' in row[4]:
                var.ui.chkTransfe.setChecked(True)
            if 'Tarjeta' in row[4]:
                var.ui.chkTarjeta.setChecked(True)
            if 'Cargo' in row[4]:
                var.ui.chkCargoCuenta.setChecked(True)
            #row[0] es el dni
            #Le pasa a onecli el dni del usuario a cargar y carga sus datos
            registro = conexion.Conexion.oneCli(row[0])
            var.ui.txtDir.setText(str(registro[0]))
            var.ui.cmbPro.setCurrentText(str(registro[1]))
            var.ui.cmbMuni.setCurrentText(str(registro[2]))
            if str(registro[3]) == 'Hombre':
                var.ui.rbtHom.setChecked(True)
            elif str(registro[3]) == 'Mujer':
                var.ui.rbtFem.setChecked(True)
        except Exception as Error:
            print('Error en guardar clientes ', Error)

    '''
    Metodo para guardar el cliente
    '''
    def guardaCli(self):
        try:
            #preparamos el registro
            newcli = []
            cliente = [var.ui.txtDNI, var.ui.txtAltaCli, var.ui.txtApel, var.ui.txtNome, var.ui.txtDir]   # para base de datos
            tabcli = []   # para tablewidget
            client =[var.ui.txtDNI, var.ui.txtApel, var.ui.txtNome, var.ui.txtAltaCli]
            # código para cargar en la tabla el cliente y la forma de pago
            for i in cliente:
                newcli.append(i.text())
            for i in client:
                tabcli.append(i.text())
            newcli.append(var.ui.cmbPro.currentText())
            newcli.append(var.ui.cmbMuni.currentText())
            if var.ui.rbtHom.isChecked():
                newcli.append('Hombre')
            else:
                newcli.append('Mujer')
            pagos = []
            if var.ui.chkCargoCuenta.isChecked():
                pagos.append('Cargo Cuenta')
            if var.ui.chkTransfe.isChecked():
                pagos.append('Transeferencia')
            if var.ui.chkTarjeta.isChecked():
                pagos.append('Tarjeta')
            if var.ui.chkEfectivo.isChecked():
                pagos.append('Efectivo')
            pagos = set(pagos)  #evita duplicados
            newcli.append('; '.join(pagos))
            tabcli.append('; '.join(pagos))
            print(newcli)
            #cargamos la tabla
            if (var.ui.lblValidoDni.text()  == 'V'):
                conexion.Conexion.altaCli(newcli)
                conexion.Conexion.cargaTabCli(self)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('DNI no válido')
                msg.exec()

            # código para grabar en la base de datos
        except Exception as error:
            print('Error en guardar clientes', error)

    '''
    Metodo para capturar los datos del cliente a modificar y pasarlo al metodo que lo modifica
    '''
    def modifCli(self):
        try:
            modcliente = []
            cliente = [var.ui.txtDNI, var.ui.txtAltaCli, var.ui.txtApel, var.ui.txtNome, var.ui.txtDir]
            for i in cliente:
                modcliente.append(i.text())
            modcliente.append(var.ui.cmbPro.currentText())
            modcliente.append(var.ui.cmbMuni.currentText())
            if var.ui.rbtHom.isChecked():
                modcliente.append('Hombre')
            else:
                modcliente.append('Mujer')
            pagos = []
            if var.ui.chkCargoCuenta.isChecked():
                pagos.append('Cargo Cuenta')
            if var.ui.chkTransfe.isChecked():
                pagos.append('Transeferencia')
            if var.ui.chkTarjeta.isChecked():
                pagos.append('Tarjeta')
            if var.ui.chkEfectivo.isChecked():
                pagos.append('Efectivo')
            pagos = set(pagos)  # evita duplicados
            modcliente.append('; '.join(pagos))
            print(modcliente)
            conexion.Conexion.modifCli(modcliente)
            conexion.Conexion.cargaTabCli(self)
        except Exception as error:
            print('Problemas en actualizar el cliente', error)


    '''
    Módulos gestión base datos cliente
    '''
    def altaCli(newcli):
        try:
            pass
        except Exception as error:
            print('Problemas en altaCliente', error)

    '''
    Metodo para pasar el dni al metodo que da de baja un cliente
    '''
    def bajaCli(self):
        try:
            dni = var.ui.txtDNI.text()
            conexion.Conexion.bajaCli(dni)
            conexion.Conexion.cargaTabCli(self)

        except Exception as error:
            print('Problemas en baja cliente', error)

    '''
    Metodo que cambia el valor de un lbl dependiendo del valor en el spin
    '''
    def envio(self):
        try:
            if var.ui.spinEnvio.value() == 0:
                var.ui.lblEnvio.setText('Recogida por cliente')
            elif var.ui.spinEnvio.value() == 1:
                var.ui.lblEnvio.setText('Envío Nacional Paquetería Express Urgente')
            elif var.ui.spinEnvio.value() == 2:
                var.ui.lblEnvio.setText('Envío Nacional Paquetería Normal')
            elif var.ui.spinEnvio.value() == 3:
                var.ui.lblEnvio.setText('Envío Interncional')
        except Exception as error:
            print('Error en modulo envío', error)


