from PySide6.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton)
from PySide6.QtCore import Signal
from controllers.action_check import ActionCheck


class RollDice(QWidget):
    total_dice_roll_value = Signal(int)

    def __init__(self, parent=None):
        super().__init__()

        self.setMaximumSize(300, 200)

        title = QLabel("Roll Dice")
        self.roll_button = QPushButton("Roll")
        die_1_label = QLabel("Die 1")
        die_2_label = QLabel("Die 2")
        self.die_1_value = QLabel("")
        self.die_2_value = QLabel("")
        current_total_label = QLabel("Current Total")
        self.current_total_value = QLabel("0")

        # Signals
        self.roll_button.pressed.connect(self._roll_dice)

        # Layouts

        die_1_layout = QVBoxLayout()
        die_1_layout.addWidget(self.die_1_value)
        die_1_layout.addWidget(die_1_label)

        die_2_layout = QVBoxLayout()
        die_2_layout.addWidget(self.die_2_value)
        die_2_layout.addWidget(die_2_label)

        dice_layout = QHBoxLayout()
        dice_layout.addLayout(die_1_layout)
        dice_layout.addLayout(die_2_layout)

        current_total_layout = QHBoxLayout()
        current_total_layout.addWidget(current_total_label)
        current_total_layout.addWidget(self.current_total_value)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addLayout(dice_layout)
        layout.addWidget(self.roll_button)
        layout.addLayout(current_total_layout)

        self.setLayout(layout)

    def _roll_dice(self):
        current_total = int(self.current_total_value.text())

        result = ActionCheck().roll_dice(current_total)

        self.die_1_value.setText(str(result["die_1"]))
        self.die_2_value.setText(str(result["die_2"]))
        self.current_total_value.setText(str(result["current_total"]))

        self.total_dice_roll_value.emit(result["current_total"])

        if ((result['die_1'] == result['die_2']) and not (result["die_1"] == 1 and result["die_2"] == 1)):
            self.roll_button.setText("Doubles! Roll Again?")
        else:
            self.roll_button.setText("Roll Complete")
            self.roll_button.setDisabled(True)
