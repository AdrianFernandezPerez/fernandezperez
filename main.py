import clients
import conexion
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
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
        var.ui.actiontoolbarsalir.triggered.connect(events.Eventos.Salir)
        var.ui.toolbarAbrirDir.triggered.connect(events.Eventos.AbrirDir)
        var.ui.toolbarBackUp.triggered.connect(events.Eventos.crearBackup)
        var.ui.actiontoolbarimprimir.triggered.connect(events.Eventos.imprimir)
        var.ui.rbtGroupSex.buttonClicked.connect(clients.Clientes.selSexo)
        var.ui.chkGroupPago.buttonClicked.connect(clients.Clientes.selPago)
        var.ui.btnGrabaCli.clicked.connect(clients.Clientes.guardaCli)
        var.ui.btnRefrescar.clicked.connect(clients.Clientes.limpiaFormCli)
        var.ui.btnBajaCli.clicked.connect(clients.Clientes.bajaCli)
        var.ui.btnModifCli.clicked.connect(clients.Clientes.modifCli)
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

        '''
        Eventos caja de texto
        '''
        var.ui.txtDNI.editingFinished.connect(clients.Clientes.validarDNI)
        var.ui.txtDNI.editingFinished.connect(clients.Clientes.mayustxt)
        var.ui.txtApel.editingFinished.connect(clients.Clientes.mayustxt)
        var.ui.txtNome.editingFinished.connect(clients.Clientes.mayustxt)
        var.ui.txtDir.editingFinished.connect(clients.Clientes.mayustxt)

        '''
        Eventos de comboBox antiguos
        clients.Clientes.cargaProv(self)
        var.ui.cmbPro.activated[str].connect(clients.Clientes.selProv)
        clients.Clientes.cargaMuni(self)
        var.ui.cmbMuni.activated[str].connect(clients.Clientes.selMuni)
        '''

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

        '''
        Base de datos
        '''
        conexion.Conexion.db_connect(var.filedb)
        conexion.Conexion.cargaTabCli(self)
        conexion.Conexion.cargaProv(self)
        var.ui.cmbPro.activated[int].connect(conexion.Conexion.cargaMuni)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - window.width()) // 2
    y = (desktop.height() - window.height()) // 2
    window.move(x, y)
    var.dlgaviso = DialogAviso()
    var.dlgcalendar = DialogCalendar()
    var.dlgabrir = FileDialogAbrir()
    window.show()
    sys.exit(app.exec())
