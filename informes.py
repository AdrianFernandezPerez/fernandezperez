import var, os
from windowordenar import *
from PyQt5 import QtSql
from reportlab.pdfgen import canvas
from datetime import datetime
import sys
import informes

class Informes():
    def listadoClientes(self):
        try:
            var.cv = canvas.Canvas('informes/listadoclientes.pdf')
            var.cv.setTitle('Listado de Clientes')
            var.cv.setAuthor('Departamento de Administración')
            rootPath = '.\\informes'
            var.cv.setFont('Helvetica-Bold', size = 9)
            textotitulo = 'LISTADO CLIENTES'
            Informes.cabecera(self)
            Informes.pie(textotitulo)
            var.cv.drawString(255,690, textotitulo)
            var.cv.line(40, 685, 530, 685)
            items = ['DNI', 'Nombre', 'Formas de Pago']
            var.cv.drawString(65, 675, items[0])
            var.cv.drawString(220, 675, items[1])
            var.cv.drawString(370, 675, items[2])
            var.cv.line(40, 670, 530, 670)
            query = QtSql.QSqlQuery()
            query.prepare('select dni, apellidos, nombre, pago from clientes order by apellidos, nombre')
            var.cv.setFont('Helvetica', size = 8)
            if query.exec_():
                i = 50
                j = 655
                while query.next():
                    if j <= 80:
                        var.cv.drawString(440, 30, 'Página siguiente...')
                        var.cv.showPage()
                        Informes.cabecera(self)
                        Informes.pie(textotitulo)
                        var.cv.drawString(255, 690, textotitulo)
                        var.cv.line(40, 685, 530, 685)
                        items = ['DNI', 'Nombre', 'Formas de Pago']
                        var.cv.drawString(65, 675, items[0])
                        var.cv.drawString(220, 675, items[1])
                        var.cv.drawString(370, 675, items[2])
                        var.cv.line(40, 670, 530, 670)
                        i = 50
                        j = 655
                    var.cv.setFont('Helvetica', size=8)
                    var.cv.drawString(i, j, str(query.value(0)))
                    var.cv.drawString(i+140, j, str(query.value(1) + ', ' + query.value(2)))
                    var.cv.drawString(i+310, j, str(query.value(3)))
                    j = j - 20

            var.cv.save()
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print("Error al listar los clientes en informes" +error)

    def listadoPro(self):
        try:
            texto = str(var.texto)
            print(texto)
            var.cv = canvas.Canvas('informes/proveedores.pdf')
            var.cv.setTitle('Listado de Proveedores')
            var.cv.setAuthor('Departamento de Administración')
            rootPath = '.\\informes'
            var.cv.setFont('Helvetica-Bold', size = 9)
            textotitulo = 'LISTADO PROVEEDORES'
            Informes.cabecera(self)
            Informes.pie(textotitulo)
            var.cv.drawString(255,690, textotitulo)
            var.cv.line(40, 685, 530, 685)
            items = ['Nombre', 'Teléfono', 'Email', 'Pago']
            var.cv.drawString(65, 675, items[0])
            var.cv.drawString(200, 675, items[1])
            var.cv.drawString(320, 675, items[2])
            var.cv.drawString(440, 675, items[3])
            var.cv.line(40, 670, 530, 670)
            query = QtSql.QSqlQuery()
            query.prepare('select nombre, telefono, email, pago from proveedores order by +'+texto)

            var.cv.setFont('Helvetica', size = 8)
            if query.exec_():
                i = 50
                j = 655
                while query.next():
                    if j <= 80:
                        var.cv.drawString(440, 30, 'Página siguiente...')
                        var.cv.showPage()
                        Informes.cabecera(self)
                        Informes.pie(textotitulo)
                        var.cv.drawString(255, 690, textotitulo)
                        var.cv.line(40, 685, 530, 685)
                        items = ['Nombre', 'Telefono', 'Email', 'Pago']
                        var.cv.drawString(65, 675, items[0])
                        var.cv.drawString(140, 675, items[1])
                        var.cv.drawString(220, 675, items[2])
                        var.cv.drawString(200, 675, items[3])
                        var.cv.line(40, 670, 530, 670)
                        i = 50
                        j = 655
                    var.cv.setFont('Helvetica', size=8)
                    var.cv.drawString(i, j, str(query.value(0)))
                    var.cv.drawString(i+145, j, str(query.value(1)))
                    var.cv.drawString(i+260, j, str(query.value(2)))
                    var.cv.drawString(i + 375, j, str(query.value(3)))
                    j = j - 20

            var.cv.save()
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print("Error al listar los proveedores en informes" +error)


    def cabecera(self):
        try:
            logo = '.\\img\logo_empresa.png'
            var.cv.line(40, 800, 530, 800)
            var.cv.setFont('Helvetica-Bold', 14)
            var.cv.drawString(50, 785, 'Import-Export Vigo')
            var.cv.setFont('Helvetica', 11)
            var.cv.drawString(50,770, 'CIF: A0000000H')
            var.cv.drawString(50, 755, 'Dirección: Avenida Galicia, 101')
            var.cv.drawString(50, 740, 'Vigo - 36216 - Spain')
            var.cv.drawString(50, 725, 'e-mail: micorreo@mail.com')
            var.cv.drawImage(logo, 425, 735)
            var.cv.line(40, 710, 530, 710)
        except Exception as error:
            print("Error en cabecera informe" + error)

    def pie(texto):
        try:
            var.cv.line(50, 50, 530, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%dd.%mm.%yyyy %H.%M.%S')
            var.cv.setFont('Helvetica', size = 6)
            var.cv.drawString(70, 40, str(fecha))
            var.cv.drawString(265, 40, str(texto))
            var.cv.drawString(490, 40, str('Página %s ' %var.cv.getPageNumber()))

        except Exception as error:
            print('Error creación de pie de informe clientes', error)

    def ordenarPor(self):
        try:
            var.dlgordenar.show()
            if var.dlgordenar.exec():
                sys.exit()
            else:
                var.dlgaviso.hide()
        except Exception as error:
            print('Error al ordenar por un campo', error)

    def obtenerTexto(texto):
        try:
            var.texto = texto
        except Exception as error:
            print('Error al obtener el dato')

