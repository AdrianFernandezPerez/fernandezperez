import articulos
import clients
import conexion
import informes
import invoice
from window import *
from windowaviso import *
from windowcal import *
from datetime import *
import sys, var, events, locale
locale.setlocale(locale.LC_ALL, 'es-ES')

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        '''
        ventana abrir explorador windows
        '''
        super (FileDialogAbrir, self).__init__()


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        '''
        ventana calendario
        '''
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_windowcal()
        var.dlgcalendar.setupUi(self)
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate((QtCore.QDate(diaactual,mesactual,anoactual)))
        var.dlgcalendar.Calendar.clicked.connect(clients.Clientes.cargarFecha)

class DialogCalendarFac(QtWidgets.QDialog):
    def __init__(self):
        '''
        ventana calendario
        '''
        super(DialogCalendarFac, self).__init__()
        var.dlgcalendarFac = Ui_windowcal()
        var.dlgcalendarFac.setupUi(self)
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendarFac.Calendar.setSelectedDate((QtCore.QDate(diaactual, mesactual, anoactual)))
        var.dlgcalendarFac.Calendar.clicked.connect(clients.Clientes.cargarFechaFactura)

class DialogAviso(QtWidgets.QDialog):
    def __init__(self):
        '''
        Clase que instancia la ventana de aviso salir
        '''
        super(DialogAviso, self).__init__()
        var.dlgaviso = Ui_Aviso()
        var.dlgaviso.setupUi(self)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)


        '''
        Eventos de botón
        '''
        var.ui.btnCalendar.clicked.connect(events.Eventos.abrircal)
        var.ui.btnCalendar_2.clicked.connect(events.Eventos.abrircalFac)
        var.ui.btnGrabaCli.clicked.connect(clients.Clientes.guardaCli)
        var.ui.btnRefrescar.clicked.connect(clients.Clientes.limpiaFormCli)
        var.ui.btnBajaCli.clicked.connect(clients.Clientes.bajaCli)
        var.ui.btnModifCli.clicked.connect(clients.Clientes.modifCli)
        var.ui.btnPdfcli.clicked.connect(informes.Informes.listadoClientes)
        var.ui.btnBuscarCliFac.clicked.connect(invoice.Facturas.buscaCli)
        var.ui.btnFacturar.clicked.connect(invoice.Facturas.facturar)

        '''
        Eventos del toolbar
        '''
        var.ui.actiontoolbarsalir.triggered.connect(events.Eventos.Salir)
        var.ui.toolbarAbrirDir.triggered.connect(events.Eventos.AbrirDir)
        var.ui.toolbarBackUp.triggered.connect(events.Eventos.crearBackup)
        var.ui.toolbarRecBackUp.triggered.connect(events.Eventos.restaurarBackup)
        var.ui.actiontoolbarimprimir.triggered.connect(events.Eventos.imprimir)

        '''
        Eventos de la barra de menús y de herramientas
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.actionAbrir.triggered.connect(events.Eventos.Abrir)
        var.ui.actionCrear_Backup.triggered.connect(events.Eventos.crearBackup)
        var.ui.actionRecuperar_Backup.triggered.connect(events.Eventos.restaurarBackup)
        var.ui.actionImprimir.triggered.connect(events.Eventos.imprimir)
        var.ui.actionExportar_Datos.triggered.connect(events.Eventos.ExportarDatos)
        var.ui.actionImportar_Datos.triggered.connect(events.Eventos.ImportarExcel)
        var.ui.actionListado_Clientes.triggered.connect(informes.Informes.listadoClientes)

        '''
        Eventos caja de texto
        '''
        var.ui.txtDNI.editingFinished.connect(clients.Clientes.validarDNI)
        var.ui.txtDNI.editingFinished.connect(clients.Clientes.mayustxt)
        var.ui.txtApel.editingFinished.connect(clients.Clientes.mayustxt)
        var.ui.txtNome.editingFinished.connect(clients.Clientes.mayustxt)
        var.ui.txtDir.editingFinished.connect(clients.Clientes.mayustxt)



        '''
        Barra de estado
        '''
        var.ui.statusbar.addPermanentWidget(var.ui.lblFecha, 1)
        day = datetime.now()
        var.ui.lblFecha.setText(day.strftime('%A, %d de %B de %Y'))

        '''
        Eventos QTabWidget
        '''
        events.Eventos.resizeTablaCli(self)
        var.ui.tabClientes.clicked.connect(clients.Clientes.cargaCli)
        var.ui.tabClientes.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabFacturas.clicked.connect(invoice.Facturas.cargaFac)
        

        '''
        Base de datos
        '''
        conexion.Conexion.db_connect(var.filedb)
        conexion.Conexion.cargaTabCli(self)
        conexion.Conexion.cargaFacs(self)
        conexion.Conexion.cargaProv(self)
        #Carga los municipios de la provincia indicada
        var.ui.cmbPro.currentIndexChanged.connect(conexion.Conexion.cargaMuni)

        '''
        Eventos combobox
        '''
        conexion.Conexion.cargaCmbproducto(self)
        var.ui.cmbProducto.currentIndexChanged.connect(invoice.Facturas.procesoVenta)

        '''
        SpinBox
        '''
        var.ui.spinEnvio.valueChanged.connect((clients.Clientes.envio))



        '''
        //////VENTANA ARTICULOS/////
        '''
        var.ui.btnRefrescarArticulo.clicked.connect(articulos.Articulos.limpiaFormArticulo)


        '''
        Eventos caja de texto
        '''
        var.ui.txtNomeArticulo.editingFinished.connect(articulos.Articulos.mayustxt)

        '''
        Eventos de boton
        '''
        var.ui.btnGrabaArticulo.clicked.connect(articulos.Articulos.guardaArticulo)
        var.ui.btnBajaArticulo.clicked.connect(articulos.Articulos.bajaArticulo)
        var.ui.btnModifArticulo.clicked.connect(articulos.Articulos.modifArticulo)
        var.ui.btnBuscaArticulo.clicked.connect(articulos.Articulos.buscArticulo)

        '''
        Eventos QTabWidget
        '''
        events.Eventos.resizeTablaArticulos(self)
        var.ui.tabArticulos.clicked.connect(articulos.Articulos.cargaArticulo)
        var.ui.tabArticulos.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

        '''
        Base de datos
        '''
        conexion.Conexion.cargaTabArt(self)




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - window.width()) // 2
    y = (desktop.height() - window.height()) // 2
    window.move(x, y)
    var.dlgaviso = DialogAviso()
    var.dlgcalendar = DialogCalendar()
    var.dlgcalendarFac = DialogCalendarFac()
    var.dlgabrir = FileDialogAbrir()
    window.show()
    sys.exit(app.exec())
