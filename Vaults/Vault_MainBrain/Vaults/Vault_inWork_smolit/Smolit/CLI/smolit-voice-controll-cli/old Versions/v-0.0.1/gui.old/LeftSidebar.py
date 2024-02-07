
from PyQt5.QtWidgets import QDockWidget, QVBoxLayout, QPushButton, QWidget, QComboBox

class LeftSidebar(QDockWidget):
    def __init__(self, parent=None):
        super(LeftSidebar, self).__init__("Linke Seitenleiste", parent)
        self.setupUI()

    def setupUI(self):
        container = QWidget()
        layout = QVBoxLayout()

        # Dropdowns und Buttons hinzufügen
        # ...

        container.setLayout(layout)
        self.setWidget(container)
