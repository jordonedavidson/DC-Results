from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from views.ov_rv import OvRv
from views.roll_result import RollResult

app = QApplication([])

window = QMainWindow()


class Main(QWidget):
    def __init__(self):
        super().__init__()

        ov_rv = OvRv()
        roll_result = RollResult()

        ov_rv.to_hit_value.connect(roll_result.recieve_to_hit_value)

        layout = QVBoxLayout()

        layout.addWidget(ov_rv)
        layout.addWidget(roll_result)

        self.setLayout(layout)


main = Main()
window.setWindowTitle("DC Heroes Action Checker")
window.setCentralWidget(main)
window.setMaximumSize(300, 600)

window.show()
app.exec()
