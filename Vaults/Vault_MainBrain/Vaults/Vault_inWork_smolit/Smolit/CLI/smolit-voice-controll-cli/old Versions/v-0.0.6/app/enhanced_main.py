
# Import necessary modules
from PyQt5.QtWidgets import QApplication
import sys
from enhanced_speech_recognition import SpeechRecognition
from enhanced_gui import MainGUI
from enhanced_command_execution import execute_command
import threading

def on_recognized_speech(text):
    # This function will be called when speech is recognized
    global main_gui
    main_gui.update_recognized_text(text)
    execute_command(text)  # Linking with command execution

def start_speech_recognition():
    sr = SpeechRecognition("path/to/model")
    sr.stream_from_microphone(on_recognized_speech)

def main():
    app = QApplication(sys.argv)
    global main_gui
    main_gui = MainGUI()
    main_gui.show()

    # Starting speech recognition in a separate thread
    speech_thread = threading.Thread(target=start_speech_recognition, daemon=True)
    speech_thread.start()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
