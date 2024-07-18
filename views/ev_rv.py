from PySide6.QtWidgets import (
    QWidget, QSpinBox, QLabel, QHBoxLayout, QVBoxLayout, QPushButton)
from controllers.action_check import ActionCheck


class EvRv(QWidget):

    def __init__(self, parent=None):
        super().__init__()

        self.setMaximumSize(300, 200)

        title = QLabel("Determine Results")
        effect_value_label = QLabel("Effect Value")
        self.effect_value = QSpinBox()
        self.effect_value.setMinimum(1)
        self.effect_value.setMaximum(100)

        resistance_value_label = QLabel("Resistance Value")
        self.resistance_value = QSpinBox()
        self.resistance_value.setMinimum(0)
        self.resistance_value.setMaximum(100)

        results_button = QPushButton("Get Results")

        results_label = QLabel("RAPs:")
        self.results_value = QLabel()

        #Styling
        title_font = title.font()
        title_font.setPointSize(16)
        title.setFont(title_font)
        label_font = results_label.font()
        label_font.setBold(True)
        label_font.setPointSize(14)
        results_label.setFont(label_font)
        raps_font = self.results_value.font()
        raps_font.setPointSize(14)
        self.results_value.setFont(raps_font)

        # Signals
        results_button.pressed.connect(self._calculate_result)

        # Layouts
        acting_layout = QVBoxLayout()
        acting_layout.addWidget(effect_value_label)
        acting_layout.addWidget(self.effect_value)

        opposing_layout = QVBoxLayout()
        opposing_layout.addWidget(resistance_value_label)
        opposing_layout.addWidget(self.resistance_value)

        values_layout = QHBoxLayout()
        values_layout.addLayout(acting_layout)
        values_layout.addLayout(opposing_layout)

        result_layout = QHBoxLayout()
        result_layout.addWidget(results_label)
        result_layout.addWidget(self.results_value)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addLayout(values_layout)
        layout.addWidget(results_button)
        layout.addLayout(result_layout)
        self.setLayout(layout)

        self.column_shifts = 0

    def reset(self):
        self.effect_value.setValue(1)
        self.resistance_value.setValue(0)
        self.results_value.setText("")

    def receive_column_shifts(self, column_shifts):
        self.column_shifts = column_shifts

    def _calculate_result(self):
        raps = ActionCheck().get_result(
            self.effect_value.value(), self.resistance_value.value(), self.column_shifts)
        self.results_value.setText(str(raps))
        #
