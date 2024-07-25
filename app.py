from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from views.av_ov import AvOv
from views.roll_result import RollResult
from views.roll_dice import RollDice
from views.ev_rv import EvRv

app = QApplication([])

window = QMainWindow()


class Main(QWidget):
    def __init__(self):
        super().__init__()

        av_ov = AvOv()
        roll_result = RollResult()
        roll_dice = RollDice()
        ev_rv = EvRv()

        av_ov.to_hit_value.connect(roll_result.recieve_to_hit_value)
        roll_dice.total_dice_roll_value.connect(
            roll_result.recieve_dice_roll_value)
        roll_result.resulting_column_shifts.connect(
            ev_rv.receive_column_shifts
        )

        layout = QVBoxLayout()

        layout.addWidget(av_ov)
        layout.addWidget(roll_dice)
        layout.addWidget(roll_result)
        layout.addWidget(ev_rv)

        self.setLayout(layout)


if __name__ == "__main__":
    main = Main()
    window.setWindowTitle("DC Heroes Action Checker")
    window.setCentralWidget(main)
    window.setMaximumSize(300, 600)

    window.show()
    app.exec()
