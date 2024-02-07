
from PyQt5.QtWidgets import QMainWindow, QApplication, QDockWidget, QVBoxLayout, QPushButton, QWidget, QLabel, QTextEdit, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
import sys

class LeftSidebar(QDockWidget):
    def __init__(self, parent=None):
        super(LeftSidebar, self).__init__("Linke Seitenleiste", parent)
        self.setupUI()

    def setupUI(self):
        container = QWidget()
        layout = QVBoxLayout()
        # Adding stylish buttons and dropdowns
        button_example = QPushButton("Beispiel")
        button_example.setFont(QFont('Arial', 12))
        layout.addWidget(button_example)
        container.setLayout(layout)
        self.setWidget(container)

class RightSidebar(QDockWidget):
    def __init__(self, parent=None):
        super(RightSidebar, self).__init__("Rechte Seitenleiste", parent)
        self.setupUI()

    def setupUI(self):
        container = QWidget()
        layout = QVBoxLayout()
        # Adding more elements for functionality
        button_settings = QPushButton("Einstellungen")
        button_settings.setFont(QFont('Arial', 12))
        layout.addWidget(button_settings)
        container.setLayout(layout)
        self.setWidget(container)

class MainGUI(QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()
        self.title = "Voice Control GUI"
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: #f5f5f5;")

        # Left Sidebar
        self.left_sidebar = LeftSidebar(self)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.left_sidebar)

        # Right Sidebar
        self.right_sidebar = RightSidebar(self)
        self.addDockWidget(Qt.RightDockWidgetArea, self.right_sidebar)

        # Speech recognition controls
        self.start_button = QPushButton("Start Listening")
        self.stop_button = QPushButton("Stop Listening")
        self.start_button.setFont(QFont('Arial', 14))
        self.stop_button.setFont(QFont('Arial', 14))
        self.start_button.clicked.connect(self.start_listening)
        self.stop_button.clicked.connect(self.stop_listening)

        # Text display for recognized speech
        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        self.text_display.setFont(QFont('Arial', 12))

        # Layout
        central_widget = QWidget()
        central_layout = QHBoxLayout(central_widget)
        central_layout.addWidget(self.start_button)
        central_layout.addWidget(self.stop_button)
        central_layout.addWidget(self.text_display)
        self.setCentralWidget(central_widget)

    def start_listening(self):
        # Start listening to speech
        pass

    def stop_listening(self):
        # Stop listening to speech
        pass

    def update_recognized_text(self, text):
        # Update the text display with recognized speech
        self.text_display.append(text)

# Running the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainGUI()
    ex.show()
    sys.exit(app.exec_())
