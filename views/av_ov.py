from PySide6.QtWidgets import (
    QWidget, QSpinBox, QLabel, QHBoxLayout, QVBoxLayout)
from PySide6.QtCore import Signal
from controllers.action_check import ActionCheck


class AvOv(QWidget):

    to_hit_value = Signal(int)

    def __init__(self, parent=None):
        super().__init__()

        self.setMaximumSize(300, 200)

        title = QLabel("Calculate To Hit Value")
        acting_value_label = QLabel("Acting Value")
        self.acting_value = QSpinBox()
        self.acting_value.setMinimum(1)
        self.acting_value.setMaximum(100)

        opposing_value_label = QLabel("Opposing Value")
        self.opposing_value = QSpinBox()
        self.opposing_value.setMinimum(0)
        self.opposing_value.setMaximum(100)

        to_hit_label = QLabel("To Hit")
        self.roll_to_hit = QLabel()

        #Styling
        title_font = title.font()
        title_font.setPointSize(16)
        title.setFont(title_font)
        label_font = to_hit_label.font()
        label_font.setBold(True)
        to_hit_label.setFont(label_font)


        # Signals
        self.acting_value.valueChanged.connect(self._calculate_to_hit)
        self.opposing_value.valueChanged.connect(self._calculate_to_hit)

        # Layouts
        acting_layout = QVBoxLayout()
        acting_layout.addWidget(acting_value_label)
        acting_layout.addWidget(self.acting_value)

        opposing_layout = QVBoxLayout()
        opposing_layout.addWidget(opposing_value_label)
        opposing_layout.addWidget(self.opposing_value)

        values_layout = QHBoxLayout()
        values_layout.addLayout(acting_layout)
        values_layout.addLayout(opposing_layout)

        to_hit_layout = QHBoxLayout()
        to_hit_layout.addWidget(to_hit_label)
        to_hit_layout.addWidget(self.roll_to_hit)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addLayout(values_layout)
        layout.addLayout(to_hit_layout)
        self.setLayout(layout)

        # Set initial value of to_hit
        self._calculate_to_hit()

    def _calculate_to_hit(self):
        to_hit = ActionCheck().get_to_hit(
            self.acting_value.value(), self.opposing_value.value())
        self.roll_to_hit.setText(str(to_hit))
        # Emit signal with to_hit value to be used in other widgets
        self.to_hit_value.emit(int(to_hit))
