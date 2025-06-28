from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QWidget

from app.core import add_shadow
from app.gui.Ui_TreeStatusWidget import Ui_TreeStatusWidget


class TreeStatusWidget(QWidget):
    _model: str
    def __init__(self, status: str, brand: str, model: str, car_num: int, pic_path: str, parent: QWidget=None):
        super().__init__(parent=parent)
        self._ui: Ui_TreeStatusWidget = Ui_TreeStatusWidget()
        self._ui.setupUi(self)

        self._model = model
        add_shadow(self._ui.widgetStatus)
        currentStyleSheet: str = self._ui.widgetStatus.styleSheet()
        if status == "verfügbar":
            currentStyleSheet += "background: rgb(204, 229, 169);"
        elif status == "vermietet":
            currentStyleSheet += "background: rgb(229, 95, 96);"
        else:
            currentStyleSheet += "background: rgb(225, 229, 83);"
        self._ui.widgetStatus.setStyleSheet(currentStyleSheet)


        self._ui.lblBrand.setText(brand)
        self._ui.lblModel.setText(model)
        self._ui.lblCarNum.setText(str(car_num).zfill(8))
        pm: QPixmap = QPixmap(pic_path)
        scaled: QPixmap = pm.scaled(
            self._ui.lblPic.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self._ui.lblPic.setPixmap(scaled)




