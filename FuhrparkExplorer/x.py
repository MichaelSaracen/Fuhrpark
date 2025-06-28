# # Copyright (C) 2022 The Qt Company Ltd.
# # SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
#
#
# """PySide6 port of the linechart example from Qt v6.x"""
#
# import sys
#
# from PySide6.QtCharts import (QBarCategoryAxis, QBarSeries, QBarSet, QChart,
#                               QChartView, QValueAxis)
# from PySide6.QtCore import Qt
# from PySide6.QtGui import QPainter
# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
#
#
# class BarChart(QWidget):
#     def __init__(self):
#         super().__init__()
#         self._set_0 = QBarSet("Cars")
#
#         self._set_0.append([1, 2, 3, 4, 5, 6])
#
#         self._series = QBarSeries()
#         self._series.append(self._set_0)
#
#         self._chart = QChart()
#         self._chart.addSeries(self._series)
#         self._chart.setTitle("Fahrzeug Buchungen")
#         self._chart.setAnimationOptions(QChart.SeriesAnimations)
#
#         self._categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
#         self._axis_x = QBarCategoryAxis()
#         self._axis_x.append(self._categories)
#         self._chart.addAxis(self._axis_x, Qt.AlignmentFlag.AlignBottom)
#         self._series.attachAxis(self._axis_x)
#
#         self._axis_y = QValueAxis()
#         self._axis_y.setRange(0, 15)
#         self._chart.addAxis(self._axis_y, Qt.AlignmentFlag.AlignLeft)
#         self._series.attachAxis(self._axis_y)
#
#         self._chart.legend().setVisible(False)
#         self._chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)
#
#         self._chart_view = QChartView(self._chart)
#         self._chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
#
#         layout: QHBoxLayout = QHBoxLayout(self)
#         layout.setContentsMargins(0,0,0,0)
#         self.setLayout(layout)
#         layout.addWidget(self._chart_view)
#
#     def set_categories(self, categories: list) -> None:
#         self._axis_x.clear()
#         self._axis_x.append(categories)
#
#     def set_values(self, values: list) -> None:
#         self._series.clear()
#
#         new_set = QBarSet("Cars")
#         new_set.append(values)
#
#         self._series.append(new_set)
#
#         self._axis_y.setRange(0, max(values))
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#
#     window = Chart()
#     window.show()
#     window.set_categories(["Hello", "World"])
#     window.resize(420, 300)
#     window.set_values([1,3])
#     sys.exit(app.exec())
#
# # from cryptography.fernet import Fernet
# #
# # def generate_key() -> bytes:
# #     return Fernet.generate_key()
# #
# # def encrypt_password(plain_password: str, key: bytes) -> str:
# #     f = Fernet(key)
# #     return f.encrypt(plain_password.encode()).decode()
# #
# # def decrypt_password(encrypted_password: str, key: bytes) -> str:
# #     f = Fernet(key)
# #     return f.decrypt(encrypted_password.encode()).decode()
# #
# # if __name__ == "__main__":
# #     key = generate_key()
# #     print(f"🔑 Master-Key (nur lokal speichern!): {key.decode()}")
# #
# #     pw = input("Passwort für Datenbank: ")
# #     encrypted = encrypt_password(pw, key)
# #     print(f"🔐 Verschlüsselt für .env: {encrypted}")
