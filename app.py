from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from views.ov_rv import OvRv

app = QApplication([])

window = QMainWindow()
layout = QVBoxLayout()
window.setWindowTitle("DC Heroes Action Checker")
window.setCentralWidget(OvRv())

window.show()
app.exec()
