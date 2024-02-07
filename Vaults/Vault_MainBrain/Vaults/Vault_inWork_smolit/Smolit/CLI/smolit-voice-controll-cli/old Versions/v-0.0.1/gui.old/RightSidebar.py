
from PyQt5.QtWidgets import QDockWidget, QVBoxLayout, QPushButton, QWidget

class RightSidebar(QDockWidget):
    def __init__(self, parent=None):
        super(RightSidebar, self).__init__("Rechte Seitenleiste", parent)
        self.setupUI()

    def setupUI(self):
        container = QWidget()
        layout = QVBoxLayout()

        # Buttons hinzufügen
        # ...

        container.setLayout(layout)
        self.setWidget(container)
