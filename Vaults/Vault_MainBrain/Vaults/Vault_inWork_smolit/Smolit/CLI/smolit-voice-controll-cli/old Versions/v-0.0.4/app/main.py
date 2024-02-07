
# Import necessary modules
from PyQt5.QtWidgets import QApplication
import sys
from enhanced_speech_recognition_kaldi import SpeechRecognition
from gui import MainGUI
from command_execution import execute_command

def main():
    app = QApplication(sys.argv)
    main_gui = MainGUI()
    main_gui.show()

    # Initialize enhanced speech recognition with appropriate parameters
    model_dir = "path/to/kaldi/model"  # Replace with the actual model directory
    speech_recognition = SpeechRecognition(model_dir)
    print("Spracherkennung läuft... Sprechen Sie einen Befehl.")
    for phrase in speech_recognition.listen():
        print(f"Erkannter Befehl: {phrase}")
        # Add logic for command execution and interaction with the GUI
        # For example, sending the phrase to the GUI or executing a command
        ...

if __name__ == "__main__":
    main()
