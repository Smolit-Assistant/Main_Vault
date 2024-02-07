  
Das Skript soll:

1. Alle Laufwerke auf dem System identifizieren.
2. Nach `.py` (Python-Dateien) und `.sh` (Bash-Skripten) suchen.
3. Gefundene Dateien in einen spezifischen Ordner kopieren, der im Verzeichnis `Documents/Scripts` auf dem jeweiligen System liegt.

Bitte beachten Sie, dass administrative Rechte erforderlich sein können, um auf alle Laufwerke und Dateien zuzugreifen, insbesondere unter Windows.

Hier ist ein grundlegendes Python-Skript, das diese Aufgabe erfüllt:

pythonCopy code

`import os import shutil import platform import glob  def find_drives():     """Find all drives on the system."""     if platform.system() == "Windows":         from string import ascii_uppercase         drives = [f"{drive}:\" for drive in ascii_uppercase if os.path.exists(f"{drive}:\")]     else:         drives = ["/"]     return drives  def find_and_copy_files(drives, file_extensions, destination_folder):     """Find and copy files with given extensions to the destination folder."""     for drive in drives:         for ext in file_extensions:             for filepath in glob.iglob(drive + '**/*' + ext, recursive=True):                 try:                     shutil.copy(filepath, destination_folder)                     print(f"Copied: {filepath}")                 except Exception as e:                     print(f"Error copying {filepath}: {e}")  def main():     # Definieren Sie die zu suchenden Dateierweiterungen     file_extensions = ['.py', '.sh']      # Zielordner bestimmen     home_folder = os.path.expanduser('~')     destination_folder = os.path.join(home_folder, 'Documents', 'Scripts')     os.makedirs(destination_folder, exist_ok=True)      # Laufwerke finden und Dateien kopieren     drives = find_drives()     find_and_copy_files(drives, file_extensions, destination_folder)  if __name__ == "__main__":     main()`

Anleitung zur Verwendung:

1. Installieren Sie Python auf Ihrem Windows- und Linux-System.
2. Speichern Sie dieses Skript in einer Datei, z.B. `script_finder.py`.
3. Führen Sie das Skript in einer Konsole oder einem Terminal aus. Möglicherweise benötigen Sie Administratorrechte.

Hinweise:

- Das Skript durchsucht alle Verzeichnisse, was je nach Anzahl und Größe der Laufwerke und Dateien lange dauern kann.
- Stellen Sie sicher, dass Sie die erforderlichen Berechtigungen haben, um auf alle Verzeichnisse zuzugreifen.
- Es wird empfohlen, das Skript zuerst in einer Testumgebung auszuführen, um unbeabsichtigte Dateikopien zu vermeiden