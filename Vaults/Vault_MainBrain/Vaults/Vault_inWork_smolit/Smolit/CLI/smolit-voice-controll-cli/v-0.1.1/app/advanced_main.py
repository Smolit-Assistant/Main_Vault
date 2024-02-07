
# Import necessary modules
from PyQt5.QtWidgets import QApplication
import sys
from advanced_speech_recognition import AdvancedSpeechRecognition
from advanced_gui import AdvancedGUI
from advanced_command_execution import advanced_execute_command
import threading

def on_advanced_recognized_speech(text):
    # Function called when speech is recognized
    global main_gui
    main_gui.update_recognized_text(text)
    advanced_execute_command(text)  # Linking with command execution

def start_advanced_speech_recognition():
    sr = AdvancedSpeechRecognition("path/to/model")
    sr.stream_from_microphone(on_advanced_recognized_speech)

def main():
    app = QApplication(sys.argv)
    global main_gui
    main_gui = AdvancedGUI()
    main_gui.show()

    # Starting speech recognition in a separate thread
    speech_thread = threading.Thread(target=start_advanced_speech_recognition, daemon=True)
    speech_thread.start()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
