from PySide6.QtWidgets import (
    QWidget, QSpinBox, QLabel, QHBoxLayout, QVBoxLayout)
from controllers.action_check import ActionCheck


class OvRv(QWidget):
    def __init__(self, parent=None):
        super(OvRv, self).__init__(parent)

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
        self.to_hit = QLabel()

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
        to_hit_layout.addWidget(self.to_hit)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addLayout(values_layout)
        layout.addLayout(to_hit_layout)
        self.setLayout(layout)

    def _calculate_to_hit(self):
        to_hit = ActionCheck().get_to_hit(
            self.acting_value.value(), self.opposing_value.value())
        self.to_hit.setText(str(to_hit))
