from datetime import datetime

import xlwt as xlwt
from PyQt5 import QtSql, QtWidgets

import clients
import var

class Conexion():

    '''
    Metodo para conectarnos a la BD
    '''
    def db_connect(filedb):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName(filedb)
            if not db.open():
                QtWidgets.QMessageBox.critical(None,
                    'No se puede abrir la base de datos.\n' 'Haz click para continuar', QtWidgets.QMessageBox.Cancel)
                return False
            else:
                print('Conexión establecida')
                return True
        except Exception as error:
            print('Problemas en conexion ', error)


    '''
    Metodo para insertar clientes
    '''
    def altaCli(newcli):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'insert into clientes (dni, alta, apellidos, nombre, direccion, provincia, municipio, sexo, pago'
                ') VALUES (:dni, :alta, :apellidos, :nombre, :direccion, :provincia, :municipio, :sexo, :pago)')
            query.bindValue(':dni', str(newcli[0]))
            query.bindValue(':alta', str(newcli[1]))
            query.bindValue(':apellidos', str(newcli[2]))
            query.bindValue(':nombre', str(newcli[3]))
            query.bindValue(':direccion', str(newcli[4]))
            query.bindValue(':provincia', str(newcli[5]))
            query.bindValue(':municipio', str(newcli[6]))
            query.bindValue(':sexo', str(newcli[7]))
            query.bindValue(':pago', str(newcli[8]))
            if query.exec_():
                print('Inserccion correcta')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Cliente dado de alta')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
                print('Error: ', query.lastError().text())
        except Exception as error:
            print('Problemas en alta cliente ', error)

    '''
    Metodo para dar de baja a un cliente
    '''
    def bajaCli(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from clientes where dni = :dni')
            query.bindValue(':dni', str(dni))
            if query.exec_():
                print('Cliente eliminado correctamente')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Cliente dado de baja')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Error en baja cliente en conexion', error)

    '''
    Metodo que carga los clientes de la bd en la tabla de clientes
    '''
    def cargaTabCli(self):
            try:
                #linea de prueba
                var.ui.tabClientes.clearContents()
                ######
                index = 0
                query = QtSql.QSqlQuery()
                query.prepare('select dni, apellidos, nombre, alta, pago from clientes order by apellidos')
                if query.exec_():
                    while query.next():
                        dni = query.value(0)
                        apellidos = query.value(1)
                        nombre = query.value(2)
                        alta = query.value(3)
                        pago = query.value(4)
                        var.ui.tabClientes.setRowCount(index+1)
                        var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                        var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                        var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                        var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(alta))
                        var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(pago))
                        index += 1

            except Exception as error:
                print('Problemas mostrar tabla clientes', error)

    '''
    Metodo el cual se le pasa el dni del cliente a cargar y te devuelve sus siguientes datos
    '''
    def oneCli(dni):
        try:
            record = []
            query = QtSql.QSqlQuery()
            query.prepare('select direccion, provincia, municipio, sexo from clientes where dni = :dni')
            query.bindValue(':dni', dni)
            if query.exec_():
                while query.next():
                    for i in range(4):
                        record.append(query.value(i))
            return record

        except Exception as error:
            print('Problemas al mostrar tabla clientes', error)

    '''
    Funcion que carga las provincias de la BD en el combobox
    '''
    def cargaProv(self):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select id, provincia from provincias')
            if query.exec_():
                var.ui.cmbPro.addItem("")
                while query.next():
                    id = str(query.value(0))
                    provincia = query.value(1)
                    var.ui.cmbPro.addItem(provincia)
        except Exception as error:
            print('Problemas al cargar las provincias de la BD')

    '''
    Funcion que carga os municipios de la BD en el combobox con el id de la provincia
    '''
    def cargaMuni(self):
        try:
            id = 0
            var.ui.cmbMuni.clear()
            provincia = var.ui.cmbPro.currentText()
            query0 = QtSql.QSqlQuery()
            query0.prepare('select id from provincias where provincia = :provincia')
            query0.bindValue(':provincia', str(provincia))
            if query0.exec_():
                while query0.next():
                    #Guardamos el id de la provincia
                    id = query0.value(0)
            query = QtSql.QSqlQuery()
            #Buscamos los municipios con el id de la provincia
            query.prepare('select municipio from municipios where provincia_id = :id')
            query.bindValue(':id', int(id))
            if query.exec_():
                var.ui.cmbMuni.addItem("")
                while query.next():
                    municipio = str(query.value(0))
                    var.ui.cmbMuni.addItem(municipio)
        except Exception as error:
            print('Problemas al cargar los municipios de la BD')


    '''
    Metodo para modificar clientes
    '''
    def modifCli(modcliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('Update clientes set alta = :alta, apellidos = :apellidos, nombre = :nombre, direccion = :direccion, '
                          'provincia = :provincia, municipio = :municipio, sexo = :sexo, pago = :pago where dni = :dni')
            query.bindValue(':dni', str(modcliente[0]))
            query.bindValue(':alta', str(modcliente[1]))
            query.bindValue(':apellidos', str(modcliente[2]))
            query.bindValue(':nombre', str(modcliente[3]))
            query.bindValue(':direccion', str(modcliente[4]))
            query.bindValue(':provincia', str(modcliente[5]))
            query.bindValue(':municipio', str(modcliente[6]))
            query.bindValue(':sexo', str(modcliente[7]))
            query.bindValue(':pago', str(modcliente[8]))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Datos modificados de Cliente')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print('Problemas al modificar el cliente', error)

    '''
    Metodo de exportación a excel
    '''
    def exportExcel(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + '_dataExport.xls')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar datos', var.copia, '(*.xls)',
                                                                options=option)
            wb = xlwt.Workbook()
            # add_sheet is used to create sheet.
            sheet1 = wb.add_sheet('Hoja 1')

            # Cabeceras
            sheet1.write(0, 0, 'DNI')
            sheet1.write(0, 1, 'APELIDOS')
            sheet1.write(0, 2, 'NOME')
            sheet1.write(0, 3, 'DIRECCION')
            sheet1.write(0, 4, 'PROVINCIA')
            sheet1.write(0, 5, 'SEXO')
            f = 1
            query = QtSql.QSqlQuery()
            query.prepare('SELECT *  FROM clientes')
            if query.exec_():
                while query.next():
                    sheet1.write(f, 0, query.value(0))
                    sheet1.write(f, 1, query.value(2))
                    sheet1.write(f, 2, query.value(3))
                    sheet1.write(f, 3, query.value(4))
                    sheet1.write(f, 4, query.value(5))
                    sheet1.write(f, 5, query.value(7))
                    f+=1
            wb.save(directorio)

        except Exception as error:
            print('Error en conexion para exportar excel ',error)

    '''
        Metodo para insertar clientes
        '''

    def altaArticulo(newarticulo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into articulos (nombre, precio_unidad'') VALUES (:nombre, :precio_unidad)')
            query.bindValue(':nombre', str(newarticulo[0]))
            query.bindValue(':precio_unidad', str(newarticulo[1]))
            if query.exec_():
                print('Inserccion correcta')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Articulo dado de alta')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
                print('Error: ', query.lastError().text())
        except Exception as error:
            print('Problemas en alta articulo ', error)

    '''
    Metodo que carga los articulos de la bd en la tabla de articulos
    '''
    def cargaTabArt(self):
        try:
            # linea de prueba
            var.ui.tabArticulos.clearContents()
            ######
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select idArticulo, nombre, precio_unidad from articulos')
            if query.exec_():
                while query.next():
                    idArt = query.value(0)
                    nombre = query.value(1)
                    precio = query.value(2)
                    var.ui.tabArticulos.setRowCount(index + 1)
                    var.ui.tabArticulos.setItem(index, 0, QtWidgets.QTableWidgetItem(str(idArt)))
                    var.ui.tabArticulos.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabArticulos.setItem(index, 2, QtWidgets.QTableWidgetItem(precio))
                    index += 1

        except Exception as error:
            print('Problemas mostrar tabla articulos', error)

    '''
        Metodo para dar de baja a un cliente
        '''

    '''
    Metodo para eliminar un articulo
    '''
    def bajaArticulo(id):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from articulos where idArticulo = :id')
            query.bindValue(':id', str(id))
            if query.exec_():
                print('Articulo eliminado correctamente')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Articulo eliminado')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Error en eliminar un articulo en conexion', error)

    '''
    Metodo para modificar articulos
    '''
    def modifArticulo(modArticulo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'Update articulos set nombre = :nombre, precio_unidad = :precio_unidad where idArticulo = :id')
            query.bindValue(':id', str(modArticulo[0]))
            query.bindValue(':nombre', str(modArticulo[1]))
            query.bindValue(':precio_unidad', str(modArticulo[2]))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Datos modificados de Articulo')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print('Problemas al modificar el articulo', error)

    '''
    Metodo para buscar articulos por su nombre
    '''
    def buscarArticulo(nombre):
        try:
            print(nombre)
            # linea de prueba
            var.ui.tabArticulos.clearContents()
            ######
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select idArticulo, nombre, precio_unidad from articulos where nombre = :nombre')
            query.bindValue(':nombre', nombre)
            if query.exec_():
                while query.next():
                    idArt = query.value(0)
                    nombre = query.value(1)
                    precio = query.value(2)
                    var.ui.tabArticulos.setRowCount(index + 1)
                    var.ui.tabArticulos.setItem(index, 0, QtWidgets.QTableWidgetItem(str(idArt)))
                    var.ui.tabArticulos.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabArticulos.setItem(index, 2, QtWidgets.QTableWidgetItem(precio))
                    index += 1
        except Exception as error:
            print('Problemas en buscar un articulo en conexion', error)