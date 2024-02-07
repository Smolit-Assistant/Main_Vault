
from PyQt5.QtWidgets import QMainWindow, Qt
from LeftSidebar import LeftSidebar
from RightSidebar import RightSidebar

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
