"""
Alle im Code benutzten Icons sind von https://fonts.google.com/icons
"""
from typing import List

from PySide6.QtCore import Slot, Signal, QThreadPool, QTimer
from PySide6.QtWidgets import QMainWindow, QWidget

from app.core import Database
from app.core.runnable import LoadAtStartRunnable, CustomerRunnable, InsertCarRunnable, CarRentedRunnable, \
    DateElapsedRunnable, ConnectionRunnable, UpdatedCustomersRunnable

from app.widgets.dialogs import SimpleDialog
from app.widgets.dialogs.AddCustomerDialog import AddCustomerDialog
from app.widgets.dialogs.NewCarDialog import NewCarDialog


class MainWindow(QMainWindow):
    sizeChanged: Signal = Signal(int, int)
    _error_dialog: SimpleDialog|None

    def __init__(self, parent: QWidget=None):
        """
        Initialisiert das Hauptfenster, richtet die UI ein und verbindet alle Signale mit ihren Slots.
        """
        from app.gui import Ui_MainWindow
        super().__init__(parent=parent)
        self._ui: Ui_MainWindow = Ui_MainWindow()
        self._ui.setupUi(self)

        self._error_dialog: SimpleDialog|None = None

        self._ui.splitterCarDisplay.setSizes([self.width()//2,self.width() * 1.5])
        self._ui.carDisplay.set_navigation_tree(self._ui.navigationTree)
        self._ui.carStatus.tree.load_status(self._ui.rentFormular.car_status)

        # Menubar Signals und Slots
        self._ui.actAddNewCar.triggered.connect(self.on_open_new_car)
        self._ui.actCustomer.triggered.connect(self.on_open_add_customer_dialog)

        self._ui.navBar.currentIndexChanged.connect(self._on_index_changed)
        # --- Tagespreis - Hinzufügen eines Datensatzes
        self._ui.rentFormular.day_price.tree.dataAdded.connect(lambda : self._on_index_changed(3))
        self._ui.navigationTree.car_tree.carRemoved.connect(self.on_car_removed)
        self._ui.carStatus.tree.statusChanged.connect(self.on_car_status_changed)

        self._ui.carStatus.tree.statusCountChanged.connect(self._ui.statistic.on_status_count_changed)

        # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ Kunden - TAB
        self._ui.customers.table.customerUpdated.connect(self.on_customer_changed)
        # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
        # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ RENT CAR - TAB
        self._ui.rentFormular.carRented.connect(self.on_car_rented)
        # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

        self.on_load_on_start()

        self._elapsed_dates_timer: QTimer = QTimer(self)
        self._elapsed_dates_timer.timeout.connect(self.on_check_connection)
        self._elapsed_dates_timer.start(5000)

    # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ NAVBAR INDEX_CHANGED
    @Slot(int)
    def _on_index_changed(self, index: int) -> None:
        """
        Wechselt die Ansicht des Hauptfensters basierend auf dem übergebenen Index.
        :param index: Index der gewählten Seite im Navigationsmenü
        """
        self._ui.navBar.set_current_index(index)
        self._ui.stackedWidget.setCurrentIndex(index)
        self._ui.rentFormular.setVisible(index == 1)
        self._ui.carDisplay.setVisible(index == 2)
        self._ui.carStatus.setVisible(index == 3)
        self._ui.rentedCardsByCustomers.setVisible(index == 4)
        self._ui.history.setVisible(index == 5)
        self._ui.statistic.setVisible(index == 6)
        self._ui.customers.setVisible(index == 7)

    # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    @Slot()
    def on_customer_changed(self) -> None:
        """
        Lädt aktualisierte Kundendaten in die Vermietungs- und Kundenübersicht.
        """
        runnable: UpdatedCustomersRunnable = UpdatedCustomersRunnable()
        # Vermietung: Customer Liste
        runnable.signals.customersLoaded.connect(self._ui.rentFormular.customer_widget.on_add_items)
        runnable.signals.rentedLoaded.connect(self._ui.rentedCardsByCustomers.on_add_items)
        QThreadPool.globalInstance().start(runnable)

    # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ LoadAtStartRunnable
    @Slot()
    def on_load_on_start(self) -> None:
        """
        Führt beim Start Ladeoperationen aus, um Fahrzeuge, Preise, Kunden und Statistiken zu initialisieren.
        """
        runnable: LoadAtStartRunnable = LoadAtStartRunnable()
        # Fahrzeug Vorschau: Tree
        runnable.signals.carsLoaded.connect(self._ui.navigationTree.load_in_tree)
        # Vermietung: Preise
        runnable.signals.pricesLoaded.connect(self.on_prices_loaded)
        # Vermietung: Customer Liste
        runnable.signals.customersLoaded.connect(self._ui.rentFormular.customer_widget.on_add_items)
        # Customers: Tabelle
        runnable.signals.customersLoaded.connect(self._ui.customers.table.on_add_items)
        # Vermietung: ComboBoxen u.a
        runnable.signals.statusLoaded.connect(self.on_car_status)
        runnable.signals.rentedLoaded.connect(self._ui.rentedCardsByCustomers.on_add_items)
        # Statistic - Marken
        runnable.signals.statisticLoaded.connect(self._ui.statistic.on_load_statistic)
        # Statistic - Modelle
        runnable.signals.statisticModelsLoaded.connect(self._ui.statistic.on_load_statistic_model)

        # Historie befüllen
        runnable.signals.historyLoaded.connect(self._ui.history.on_load_history)
        QThreadPool.globalInstance().start(runnable)

    # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ TIMER ELAPSED DATES
    @Slot()
    def on_check_connection(self) -> None:
        """
        Überprüft periodisch die Datenbankverbindung und reagiert auf Verbindungsfehler.
        """
        try:
            runnable: ConnectionRunnable = ConnectionRunnable()
            runnable.signals.statusOk.connect(self.on_elapsed_dates)
            runnable.signals.errorOccurred.connect(self.on_connection_error)
            QThreadPool.globalInstance().start(runnable)
        except RuntimeError as e:
            print(e)

    @Slot(str)
    def on_connection_error(self, _error: str) -> None:
        """
        Öffnet einen Fehlerdialog, wenn die Verbindung zur Datenbank unterbrochen wurde.
        :param _error: Beschreibung des Verbindungsfehlers
        """
        if self._error_dialog is None:
            self._error_dialog = SimpleDialog(
                "Verbindung verloren",
                "Ein **Fehler** ist aufgetreten! Die Verbindung zum MySQL - Server wurde **unterbrochen**. Überprüfe die Verbindung" ,
                self
            )
            self._error_dialog.show_buttons(False)
            self.sizeChanged.connect(self._error_dialog.resize)


    @Slot()
    def on_elapsed_dates(self) -> None:
        """
        Prüft, ob Mietzeiträume abgelaufen sind, setzt ggf. Status zurück und aktualisiert die Ansicht.
        """
        if self._error_dialog:
            self._error_dialog.close()
            self._error_dialog = None

        car_ids: List[int] = self._ui.rentedCardsByCustomers.elapsed_dates()
        if car_ids:
            runnable: DateElapsedRunnable = DateElapsedRunnable(car_ids)
            runnable.signals.finished.connect(self.on_load_on_start)
            QThreadPool.globalInstance().start(runnable)

    # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ FAHRZEUG VERMIETEN
    # CarRentedRunnable
    @Slot(int, str, str, str, float)
    def on_car_rented(self, customer_id: int, model_name: str, from_date: str, to_data: str, total_price: float) -> None:
        """
        Behandelt das Ereignis einer Fahrzeugvermietung und startet das entsprechende Runnable.
        :param customer_id: ID des Kunden
        :param model_name: Modellname des Fahrzeugs
        :param from_date: Mietbeginn
        :param to_data: Mietende
        :param total_price: Gesamtpreis der Vermietung
        """
        runnable: CarRentedRunnable = CarRentedRunnable(customer_id, model_name, from_date, to_data, total_price)
        QThreadPool.globalInstance().start(runnable)
        runnable.signals.statusLoaded.connect(self.on_car_status)
        runnable.signals.rentedLoaded.connect(self._ui.rentedCardsByCustomers.on_add_items)
        self._on_index_changed(4)

    # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

    @Slot(list)
    def on_car_status(self, data) -> None:
        """
        Aktualisiert Fahrzeugstatus-Ansicht und Vermietungsformular mit neuen Statusdaten.
        :param data: Liste der aktuellen Statusinformationen
        """
        self._ui.rentFormular.on_load_car_status(data)
        self._ui.carStatus.tree.load_status(self._ui.rentFormular.car_status)

    @Slot()
    def on_car_status_changed(self) -> None:
        """
        Reagiert auf Statusänderung eines Fahrzeugs, indem es die Statusdaten neu lädt.
        """
        runnable: LoadAtStartRunnable = LoadAtStartRunnable()
        runnable.signals.statusLoaded.connect(self.on_car_status)
        QThreadPool.globalInstance().start(runnable)

    @Slot(str)
    def on_car_removed(self, _model: str) -> None:
        """
        Aktualisiert die Ansicht nach dem Entfernen eines Fahrzeugs.
        :param _model: Modellbezeichnung des entfernten Fahrzeugs
        """
        self.on_load_on_start()

    @Slot()
    def on_open_new_car(self) -> None:
        """
        Öffnet den Dialog zum Hinzufügen eines neuen Fahrzeugs.
        """
        self.dialog = NewCarDialog()
        self.dialog.carInserted.connect(self.on_new_card_added)
        # self.sizeChanged.connect(dialog.resize)

    @Slot()
    def on_car_inserted(self):
        """
        Callback nach erfolgreichem Einfügen eines neuen Fahrzeugs.
        """
        self.on_load_on_start()

    @Slot(list)
    def on_new_card_added(self, car: list) -> None:
        """
        Startet das Runnable zum Einfügen eines neuen Fahrzeugs in die Datenbank.
        :param car: Fahrzeugdaten
        """
        runnable: InsertCarRunnable = InsertCarRunnable(*car)
        runnable.signals.finished.connect(self.on_load_on_start)
        QThreadPool.globalInstance().start(runnable)

    @Slot(list)
    def on_prices_loaded(self, prices: list) -> None:
        """
        Lädt Tagespreise in das Vermietungsformular.
        :param prices: Liste der Tagespreise
        """
        self._ui.rentFormular.day_price.tree.on_load_day_prices(prices)
        self._ui.rentFormular.set_prices(self._ui.rentFormular.day_price.tree.price_dict)

    @Slot()
    def on_open_add_customer_dialog(self) -> None:
        """
        Öffnet den Dialog zum Hinzufügen eines neuen Kunden.
        """
        self.customer_dialog: AddCustomerDialog = AddCustomerDialog()
        self.customer_dialog.inserted.connect(self.on_customer_added)
        # self.sizeChanged.connect(dialog.resize)

    @Slot(list)
    def on_customer_added(self, customer: List) -> None:
        """
        Startet das Runnable zum Einfügen eines neuen Kunden in die Datenbank.
        :param customer: Kundendaten
        """
        runnable: CustomerRunnable = CustomerRunnable(*customer)
        runnable.signals.finished.connect(self._ui.rentFormular.customer_widget.on_add_items)
        runnable.signals.finished.connect(self._ui.customers.table.on_add_items)
        QThreadPool.globalInstance().start(runnable)

    def closeEvent(self, event, /):
        """
        Stoppt Timer und schließt die Datenbankverbindung beim Schließen des Fensters.
        :param event:
        :return:
        """
        self._elapsed_dates_timer.stop()
        Database.close()
        event.accept()


    def resizeEvent(self, event, /) -> None:
        """
        Emitiert das Signal sizeChanged bei jeder Fenstergrößeänderung.
        :param event: Resize-Event-Objekt
        :return:
        """
        self.sizeChanged.emit(event.size().width(), event.size().height())



