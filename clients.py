'''
Funciones gestion clientes
'''

import var
from window import *

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