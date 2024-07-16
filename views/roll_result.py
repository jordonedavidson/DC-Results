from PySide6.QtWidgets import (
    QWidget, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QPushButton)
from controllers.action_check import ActionCheck


class RollResult(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.setMaximumSize(300, 200)

        title = QLabel("Roll Result")

        rolled_label = QLabel("Rolled")
        self.rolled = QLineEdit()
        self.rolled.setMaxLength(3)

        results_label = QLabel("Results")
        success_label = QLabel("Success")
        self.success_value = QLabel()
        column_shifts_label = QLabel("Column Shifts")
        self.column_shifts_value = QLabel()

        success_check_button = QPushButton("Results")

        self.to_hit_value = None

        # Signals
        success_check_button.pressed.connect(self.get_results)

        # Layouts
        rolled_layout = QHBoxLayout()
        rolled_layout.addWidget(rolled_label)
        rolled_layout.addWidget(self.rolled)

        success_layout = QHBoxLayout()
        success_layout.addWidget(success_label)
        success_layout.addWidget(self.success_value)

        column_shifts_layout = QHBoxLayout()
        column_shifts_layout.addWidget(column_shifts_label)
        column_shifts_layout.addWidget(self.column_shifts_value)

        results_layout = QVBoxLayout()
        results_layout.addWidget(results_label)
        results_layout.addLayout(success_layout)
        results_layout.addLayout(column_shifts_layout)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addLayout(rolled_layout)
        layout.addWidget(success_check_button)
        layout.addLayout(results_layout)

        self.setLayout(layout)

    def recieve_to_hit_value(self, to_hit):
        print(f"Recieved To Hit Value: {to_hit}")
        self.to_hit_value = to_hit

    def get_results(self):
        print(f"To Hit: {self.to_hit_value}, Rolled: {self.rolled.text()}")
        if self.to_hit_value is not None:
            result = ActionCheck().attack_result(self.to_hit_value, int(self.rolled.text()))
            self.success_value.setText(str(result["success"]))
            self.column_shifts_value.setText(str(result["column_shifts"]))
