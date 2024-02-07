
from PyQt5.QtWidgets import QMainWindow, QApplication, QDockWidget, QVBoxLayout, QPushButton, QWidget, QComboBox, Qt
import sys

class LeftSidebar(QDockWidget):
    def __init__(self, parent=None):
        super(LeftSidebar, self).__init__("Linke Seitenleiste", parent)
        self.setupUI()

    def setupUI(self):
        container = QWidget()
        layout = QVBoxLayout()
        # Dropdowns und Buttons hinzufügen
        container.setLayout(layout)
        self.setWidget(container)

class RightSidebar(QDockWidget):
    def __init__(self, parent=None):
        super(RightSidebar, self).__init__("Rechte Seitenleiste", parent)
        self.setupUI()

    def setupUI(self):
        container = QWidget()
        layout = QVBoxLayout()
        # Buttons hinzufügen
        container.setLayout(layout)
        self.setWidget(container)

class MainGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Voice Control GUI')
        self.setGeometry(100, 100, 800, 600)
        self.setLeftSidebar()
        self.setRightSidebar()

    def setLeftSidebar(self):
        self.left_sidebar = LeftSidebar(self)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.left_sidebar)

    def setRightSidebar(self):
        self.right_sidebar = RightSidebar(self)
        self.addDockWidget(Qt.RightDockWidgetArea, self.right_sidebar)
