
from PyQt5.QtWidgets import QApplication
import sys
from speech_recognition import SpeechRecognition
from gui import MainGUI
from command_execution import execute_command

def main():
    app = QApplication(sys.argv)
    main_gui = MainGUI()
    main_gui.show()

    speech_recognition = SpeechRecognition()
    print("Spracherkennung läuft... Sprechen Sie einen Befehl.")
    for phrase in speech_recognition.listen():
        print(f"Erkannter Befehl: {phrase}")

        if phrase.lower().strip() == "shut-up":
            print("Beende Spracherkennung.")
            break

        # Beispiel für die Befehlsverarbeitung
        argument, command = "Beispielargument", "Beispielbefehl"
        response = execute_command(argument, command)
        print(response)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
