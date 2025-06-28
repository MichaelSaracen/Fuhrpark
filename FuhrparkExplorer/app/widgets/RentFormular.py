from typing import Dict

from PySide6.QtCore import Slot, QDate, Signal, Qt
from PySide6.QtWidgets import QWidget, QTreeWidgetItem

from app.core import DataMapper
from app.gui.Ui_RentFormular import Ui_RentFormular


class RentFormular(QWidget):
    # kunde_id, model_name, datum begin, datum end, total_price
    carRented: Signal = Signal(int, str, str, str, float)

    _available: dict
    _car_status: dict
    _current_price: float
    _from_date: str
    _prices: dict
    _to_date: str
    _total_price: float

    def __init__(self, parent: QWidget=None):
        super().__init__(parent=parent)
        self._ui: Ui_RentFormular = Ui_RentFormular()
        self._ui.setupUi(self)

        self._from_date = str()
        self._to_date = str()
        self._current_price = 0.0
        self._total_price = 0.0
        self._available = {}
        self._car_status = {}
        self._prices = {}
        self.on_data_changed()

        self._ui.cbBrand.currentTextChanged.connect(self.on_brand_changed)
        self._ui.cbModel.currentTextChanged.connect(self.on_model_changed)
        self._ui.sbDays.valueChanged.connect(self.on_day_count_changed)
        self._ui.rentCustomerWidget.customerIDSelected.connect(self.on_customer_id_selected)
        self._ui.btnRent.clicked.connect(self.on_rent)
        self._ui.cwFrom.selectionChanged.connect(self.on_data_changed)
        self._ui.cwTo.selectionChanged.connect(self.on_data_changed)
        self._ui.dayPrice.tree.priceChanged.connect(self.on_price_changed)
        self._ui.dayPrice.tree.currentItemChanged.connect(self.on_price_item_changed)

    @property
    def car_status(self) -> Dict:
        """
        Lädt den Status der Fahrzeuge.
        Das passiert in der **_car_status** methode, dort wird dieser zugewiesen.
        :return:
        """
        return self._car_status

    @property
    def customer_widget(self) -> None:
        """
        Liefert das Kunden-Auswahl-Widget zurück.
        """
        return self._ui.rentCustomerWidget

    @property
    def day_price(self) -> None:
        """
        Liefert das DayPrice-Widget zurück, das Preise anzeigt.
        """
        return self._ui.dayPrice

    def get_price(self) -> float:
        """
        Ermittelt den Tagespreis für das aktuell ausgewählte Fahrzeug (Marke und Modell).
        :return: Tagespreis als float
        """
        try:
            brand: str = self._ui.cbBrand.currentText()
            model: str = self._ui.cbModel.currentText()
            return self._prices[brand][model]
        except KeyError:
            return 0.0

    @Slot(QTreeWidgetItem, QTreeWidgetItem)
    def on_price_item_changed(self, current: QTreeWidgetItem, _prev: QTreeWidgetItem) -> None:
        """
        Reagiert auf Auswahländerungen im Preis-Baum und aktualisiert die Marken- und Modell-ComboBox.
        :param current: Ausgewähltes QTreeWidgetItem
        :param _prev: Vorheriges QTreeWidgetItem (unbenutzt)
        """

        if not current.parent():
            return

        brand: str = current.data(0, Qt.ItemDataRole.UserRole)
        model: str = current.data(0, Qt.ItemDataRole.UserRole + 1)

        if brand not in list(self._available.keys()):
            return

        model_keys = list(self._available.get(brand))

        if not model_keys or model not in model_keys:
            return

        self.on_brand_changed(brand)
        self._ui.cbBrand.setCurrentText(brand)
        self.on_model_changed(model)
        self._ui.cbModel.setCurrentText(model)

    @Slot(list)
    def on_load_car_status(self, data: list) -> None:
        """
        Lädt Verfügbarkeitsdaten der Fahrzeuge und füllt die Brand-ComboBox.
        :param data: Liste von Statusdaten aus der Datenbank
        """
        self._ui.cbBrand.clear()
        self._car_status = DataMapper.map_to_nested_car_status(data)
        self._available = self._car_status.get("verfügbar")
        if self._available:
            brands: set = set(self._available.keys())
            self._ui.cbBrand.addItems(list(brands))
            self.on_brand_changed(self._ui.cbBrand.currentText())
            self.on_model_changed(self._ui.cbModel.currentText())


    @Slot(str)
    def on_brand_changed(self, brand) -> None:
        """
        Aktualisiert die Modell-ComboBox basierend auf der ausgewählten Marke.
        :param brand: Name der Marke
        """
        self._ui.cbModel.clear()
        models: dict = self._available.get(brand)
        if models:
            self._ui.cbModel.addItems(set(models.keys()))

    @Slot(int)
    def on_customer_id_selected(self, c_id: int) -> None:
        """
        Setzt die Kundennummer im Eingabefeld, sobald ein Kunde ausgewählt wurde.
        :param c_id: Eindeutige Kunden-ID
        """
        self._ui.leCustomerID.setText(str(c_id).zfill(8))

    @Slot(str)
    def on_model_changed(self, _model: str) -> None:
        """
        Aktualisiert Preis-Informationen, wenn sich das Fahrzeugmodell ändert.
        :param _model: Modellname des Fahrzeugs
        """
        self._current_price = self.get_price()
        self._total_price = float(self._current_price * self._ui.sbDays.value())
        self._ui.lePricePerDay.setText(f"{self._current_price:.2f}€")
        self._ui.lblTotalPrice.setText(f"{self._total_price:.2f}")

    @Slot(int)
    def on_day_count_changed(self, days: int) -> None:
        """
        Berechnet den Gesamtpreis neu, wenn sich die Anzahl der Miettage ändert.
        :param days: Anzahl der Miettage
        """
        self._total_price = float(self._current_price * days)
        self._ui.lblTotalPrice.setText(f"{self._total_price:.2f}")

    @Slot()
    def on_rent(self) -> None:
        """
        Löst die Vermietung aus, wenn Kunde und Modell gültig sind, und sendet das carRented-Signal.
        """
        text: str = self._ui.leCustomerID.text()
        model: str = self._ui.cbModel.currentText()
        if not text or not model:
            return

        customer_id: int = int(text)
        self.carRented.emit(customer_id, model, self._from_date, self._to_date, self._total_price)
        self._ui.leCustomerID.clear()

    @Slot()
    def on_data_changed(self) -> None:
        """
        Synchronisiert Datumsauswahl, berechnet Mietdauer und verhindert ungültige Datumsangaben.
        """
        from_date = self._ui.cwFrom.selectedDate()
        to_date = self._ui.cwTo.selectedDate()
        current_date = QDate.currentDate()

        if from_date < current_date:
            self._ui.cwFrom.setSelectedDate(current_date)

        if to_date <= from_date:
            to_date = from_date.addDays(1)
            self._ui.cwTo.setSelectedDate(to_date)

        days: int = from_date.daysTo(to_date)

        if days > 100:
            to_date = from_date.addDays(100)
            self._ui.cwTo.setSelectedDate(to_date)
            days = 100

        self._ui.sbDays.setValue(days)
        self._from_date = from_date.toString("yyyy-MM-dd")
        self._to_date = to_date.toString("yyyy-MM-dd")


    @Slot(str, str, float)
    def on_price_changed(self, brand: str, model: str, price: float) -> None:
        """
        Aktualisiert den Preis für ein Modell und passt Gesamtpreis an, falls aktuell ausgewählt.
        :param brand: Name der Marke
        :param model: Modellname des Fahrzeugs
        :param price: Neuer Tagespreis
        """
        if brand not in self._prices:
            return

        if model not in self._prices[brand]:
            return


        self._prices[brand][model] = price
        if model == self._ui.cbModel.currentText():
            self._current_price = self._prices[brand][model]
            self._total_price = float(self._current_price * self._ui.sbDays.value())
            self._ui.lePricePerDay.setText(f"{self._current_price:.2f}€")
            self._ui.lblTotalPrice.setText(f"{self._total_price:.2f}")


    def set_prices(self, prices: Dict) -> None:
        """
        Setzt die Preisübersicht für alle Marken und Modelle.
        :param prices: Verschachteltes Dictionary mit Marken- und Modellpreisen
        """
        self._prices = prices

