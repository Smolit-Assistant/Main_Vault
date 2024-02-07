
from PyQt5.QtWidgets import QApplication
from MainGUI import MainGUI
import sys

def main():
    app = QApplication(sys.argv)
    main_gui = MainGUI()
    main_gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
