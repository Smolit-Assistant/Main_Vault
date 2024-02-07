
# Import necessary modules
from PyQt5.QtWidgets import QApplication
import sys
from enhanced_speech_recognition_kaldi import SpeechRecognition
from gui import MainGUI
from command_execution import execute_command

def on_recognized_speech(text):
    # This function will be called when speech is recognized
    main_gui.update_recognized_text(text)
    execute_command(text)  # Linking with command execution

def main():
    app = QApplication(sys.argv)
    global main_gui
    main_gui = MainGUI()

    # Initialize enhanced speech recognition with appropriate parameters
    model_dir = "path/to/kaldi/model"  # Replace with the actual model directory
    global speech_recognition
    speech_recognition = SpeechRecognition(model_dir)
    main_gui.set_speech_recognition_callbacks(speech_recognition.continuous_listen, on_recognized_speech)

    main_gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
