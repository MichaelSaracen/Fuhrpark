"""
Alle Icons die in dieser Anwendung benutzt werden, sind von:
https://fonts.google.com/icons
"""

__author__ = "Michael Saracen"
__version__ = "1.0.0" # Major.Minor.Patch

import sys

from PySide6.QtCore import Slot, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QApplication, QWidget

from app.core import Database
from app.gui.Ui_Login import Ui_Login
from app.widgets import MainWindow


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self._ui: Ui_Login = Ui_Login()
        self._ui.setupUi(self)

        self._ui.btnSubmit.clicked.connect(self.on_submit)
        self._ui.leUser.textChanged.connect(self.on_text_changed)
        self._ui.leUser.returnPressed.connect(self.on_submit)
        self._ui.lePassword.textChanged.connect(self.on_text_changed)
        self._ui.lePassword.returnPressed.connect(self.on_submit)

        validator = QRegularExpressionValidator(QRegularExpression(r"^[a-zA-Z0-9#+\-@§$%&()*!?]+$"))
        self._ui.lePassword.setValidator(validator)


    @Slot(str)
    def on_text_changed(self, _text: str):
        self._ui.btnSubmit.setEnabled(len(self._ui.leUser.text()) > 2 and len(self._ui.lePassword.text()) > 6)

    @Slot()
    def on_submit(self) -> None:
        """
        Submit Handling. Wird der Button gedrückt, wird überprüft, ob die eingegebenen Daten
        korrekt sind.
        :return:
        """
        if not self._ui.btnSubmit.isEnabled():
            return

        Database.check_connection(
            self._ui.leUser.text(),
            self._ui.lePassword.text(),
            self._success_login,
            self._login_fail
        )

    def _success_login(self) -> None:
        """
        Wenn der Login erfolgreich war, wird das MainWindow geöffnet.
        :return:
        """
        mw: MainWindow = MainWindow()
        mw.show()
        self.close()

    def _login_fail(self) -> None:
        """
        Wenn der Login fehlschlug, erscheint die Nachricht, dass das Passwort und Benutzername
        überprüft werden soll.
        :return:
        """
        self._ui.lblError.setText("Fehlerhafte Eingabe. Überprüfe Passwort und Benutzernamen!")

if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    login: Login = Login()
    login.show()

    app.exec()