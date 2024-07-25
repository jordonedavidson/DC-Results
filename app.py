from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from views.av_ov import AvOv
from views.roll_result import RollResult
from views.roll_dice import RollDice
from views.ev_rv import EvRv

app = QApplication([])

window = QMainWindow()


class Main(QWidget):
    def __init__(self):
        super().__init__()

        reset_button = QPushButton("Reset")

        self.av_ov = AvOv()
        self.roll_result = RollResult()
        self.roll_dice = RollDice()
        self.ev_rv = EvRv()

        self.av_ov.to_hit_value.connect(self.roll_result.recieve_to_hit_value)
        self.roll_dice.total_dice_roll_value.connect(
            self.roll_result.recieve_dice_roll_value)
        self.roll_result.resulting_column_shifts.connect(
            self.ev_rv.receive_column_shifts
        )

        reset_button.clicked.connect(self._reset)

        layout = QVBoxLayout()

        layout.addWidget(self.av_ov)
        layout.addWidget(self.roll_dice)
        layout.addWidget(self.roll_result)
        layout.addWidget(self.ev_rv)
        layout.addWidget(reset_button)

        self.setLayout(layout)

    def _reset(self):
        self.av_ov.reset()
        self.roll_result.reset()
        self.roll_dice.reset()
        self.ev_rv.reset()


if __name__ == "__main__":
    main = Main()
    window.setWindowTitle("DC Heroes Action Checker")
    window.setCentralWidget(main)
    window.setMaximumSize(300, 600)

    window.show()
    app.exec()
