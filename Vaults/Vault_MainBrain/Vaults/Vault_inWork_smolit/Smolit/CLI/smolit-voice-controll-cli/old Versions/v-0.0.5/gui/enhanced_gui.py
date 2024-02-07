
from PyQt5.QtWidgets import QMainWindow, QApplication, QDockWidget, QVBoxLayout, QPushButton, QWidget, QLabel, QTextEdit, QHBoxLayout
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
        # Dropdowns und Buttons hinzufügen
        container.setLayout(layout)
        self.setWidget(container)

class MainGUI(QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()
        self.setWindowTitle("Voice Control System")
        self.setGeometry(100, 100, 800, 600)
        self.setupUI()

    def setupUI(self):
        self.text_display = QTextEdit(self)
        self.text_display.setReadOnly(True)
        self.setCentralWidget(self.text_display)

        self.left_sidebar = LeftSidebar(self)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.left_sidebar)

        self.right_sidebar = RightSidebar(self)
        self.addDockWidget(Qt.RightDockWidgetArea, self.right_sidebar)

        self.start_button = QPushButton("Start Listening", self)
        self.start_button.clicked.connect(self.start_listening)
        self.left_sidebar.layout().addWidget(self.start_button)

        self.stop_button = QPushButton("Stop Listening", self)
        self.stop_button.clicked.connect(self.stop_listening)
        self.left_sidebar.layout().addWidget(self.stop_button)

    def update_recognized_text(self, text):
        self.text_display.append(text)

    def set_speech_recognition_callbacks(self, listen_callback, recognized_callback):
        self.listen_callback = listen_callback
        self.recognized_callback = recognized_callback

    def start_listening(self):
        # Start speech recognition
        self.listen_callback(self.recognized_callback)

    def stop_listening(self):
        # Logic to stop speech recognition
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainGUI()
    window.show()
    sys.exit(app.exec_())
