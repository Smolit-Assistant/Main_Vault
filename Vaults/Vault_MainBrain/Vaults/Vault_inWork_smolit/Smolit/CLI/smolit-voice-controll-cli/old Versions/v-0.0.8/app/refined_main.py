
# Import necessary modules
from PyQt5.QtWidgets import QApplication
import sys
from refined_speech_recognition import RefinedSpeechRecognition
from refined_gui import MainGUI
from refined_command_execution import refined_execute_command
import threading

def on_refined_recognized_speech(text):
    # This function will be called when speech is recognized
    global main_gui
    main_gui.update_recognized_text(text)
    refined_execute_command(text)  # Linking with command execution

def start_refined_speech_recognition():
    sr = RefinedSpeechRecognition("path/to/model")
    sr.stream_from_microphone(on_refined_recognized_speech)

def main():
    app = QApplication(sys.argv)
    global main_gui
    main_gui = MainGUI()
    main_gui.show()

    # Starting speech recognition in a separate thread
    speech_thread = threading.Thread(target=start_refined_speech_recognition, daemon=True)
    speech_thread.start()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
