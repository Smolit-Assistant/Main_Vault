
import threading
import sys
from PyQt5.QtWidgets import QApplication
# Importieren der GUI-Komponenten aus dem 'gui'-Unterordner
from gui.MainGUI import MainGUI
from pocketsphinx import LiveSpeech, get_model_path

def execute_command(argument, command):
    full_command = f"sgpt {argument} {command}"
    try:
        output = subprocess.check_output(full_command, shell=True, stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei der Ausführung des Befehls: {e.output.decode()}")

def parse_command(phrase):
    words = phrase.split()
    if len(words) > 2 and words[0].lower() == "sgpt":
        return words[1], " ".join(words[2:])
    else:
        return None, None

# def create_microphone_popup():
#    window = tk.Tk()
#    window.title("Spracherkennung Aktiv")

    # Laden Sie hier Ihr Mikrofonsymbol-Bild
#    mic_image = PhotoImage(file="microphone_icon.png")
#    label = tk.Label(window, image=mic_image)
#    label.pack()

#    window.mainloop()

def main():
    # Starten Sie die GUI in einem separaten Thread
#    gui_thread = threading.Thread(target=create_microphone_popup)
#    gui_thread.start()

#    model_path = get_model_path()
#    speech = LiveSpeech(
#        verbose=False,
#        sampling_rate=16000,
#        buffer_size=2048,
#        no_search=False,
#        full_utt=False,
#        hmm=os.path.join(model_path, 'en-us'),
#        lm=os.path.join(model_path, 'en-us.lm.bin'),
#        dic=os.path.join(model_path, 'cmudict-en-us.dict')
#    )
    app = QApplication(sys.argv)
    main_gui = MainGUI()
    main_gui.show()
    sys.exit(app.exec_())

    print("Spracherkennung läuft... Sprechen Sie einen Befehl.")
    for phrase in speech:
        phrase_str = str(phrase)
        print(f"Erkannter Befehl: {phrase_str}")

        if phrase_str.lower().strip() == "shut-up":
            print("Beende Spracherkennung.")
            break

        argument, command = parse_command(phrase_str)
        if argument:
            execute_command(argument, command)

    # Beenden Sie das Tkinter-Fenster, wenn die Spracherkennung beendet wird
    tk._default_root.quit()

if __name__ == "__main__":
    main()
