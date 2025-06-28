from typing import List, Tuple, Any

from PySide6.QtCore import Slot, Signal, QThreadPool
from PySide6.QtGui import QPixmap, Qt, QShortcut, QKeySequence
from PySide6.QtWidgets import QWidget, QFileDialog

from app.core import DataMapper
from app.core.runnable import InitFieldRunnable
from app.gui.Ui_NewCarDialog import Ui_NewCarDialog


class NewCarDialog(QWidget):
    carInserted: Signal = Signal(list)
    inserted: Signal = Signal()
    _image_path: str

    def __init__(self, parent: QWidget=None):
        super().__init__(parent=parent)
        self._ui: Ui_NewCarDialog = Ui_NewCarDialog()
        self._ui.setupUi(self)

        self._init_fields()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        # self.resize(parent.width(), parent.height())
        # add_shadow(self._ui.widget)
        self.show()
        esc_shortcut: QShortcut = QShortcut(QKeySequence("ESC"), self)
        esc_shortcut.activated.connect(self.close)

        self._image_path = ""

        self._ui.btnLoadImage.clicked.connect(self.on_load_image)
        self._ui.leModel.textChanged.connect(self.on_enable_save)
        self._ui.leColor.textChanged.connect(self.on_enable_save)
        self._ui.btnSave.clicked.connect(self.on_save_car)


    @Slot()
    def on_load_image(self):
        path: str = QFileDialog.getOpenFileName(self, "Bild auswählen", "", "PNG(*.png)")[0]
        if path:
            self._image_path = path
            pm = QPixmap(path)
            scaled_pixmap = pm.scaled(
                self._ui.lblImage.rect().size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self._ui.lblImage.setPixmap(scaled_pixmap)
            self.on_enable_save()

    @Slot()
    def on_enable_save(self):
        enabled: bool = all([self._image_path, self._ui.leColor.text(), self._ui.leModel.text()] )
        self._ui.btnSave.setEnabled(enabled)

    @Slot()
    def on_save_car(self) -> None:


        self.carInserted.emit(
            [
                self._image_path, self._ui.cbBrand.currentText(), self._ui.leModel.text(),
                self._ui.cbFuel.currentText(), self._ui.cbGearbox.currentText(), self._ui.sbPower.value(),
                self._ui.sbConsum.value(), self._ui.sbDoors.value(), self._ui.sbSeats.value(), self._ui.leColor.text(),
                str(self._ui.sbPrice.value())
            ]
        )
        self.inserted.emit()
        self.close()

    def _init_fields(self):
        runnable: InitFieldRunnable = InitFieldRunnable()
        runnable.signals.finished.connect(self._on_fields_loaded)
        QThreadPool.globalInstance().start(runnable)

    @Slot(list)
    def _on_fields_loaded(self, result: List[List[Tuple[Any]]]):
        fuels, brands, gearboxes = result
        self._ui.cbFuel.addItems(DataMapper.extract_first_rows(fuels))
        self._ui.cbBrand.addItems(DataMapper.extract_first_rows(brands))
        self._ui.cbGearbox.addItems(DataMapper.extract_first_rows(gearboxes))

    # def _init_fields(self):
    #
    #     fuels, brands, gearboxes = Database.call_procedures(
    #         ["p_get_fuel", "p_get_brands", "p_get_gearbox"]
    #     )
    #
    #     self._ui.cbFuel.addItems(DataMapper.extract_first_rows(fuels))
    #     self._ui.cbBrand.addItems(DataMapper.extract_first_rows(brands))
    #     self._ui.cbGearbox.addItems(DataMapper.extract_first_rows(gearboxes))






