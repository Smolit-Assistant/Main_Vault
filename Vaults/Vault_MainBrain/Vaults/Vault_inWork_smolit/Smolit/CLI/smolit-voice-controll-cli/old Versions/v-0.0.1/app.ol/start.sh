#!/bin/bash

# Aktivieren der virtuellen Umgebung
source venv/bin/activate

# Ausf�hren des Haupt-Python-Skripts
python app.py

# Deaktivieren der virtuellen Umgebung
deactivate

echo "Voice-Control beendet."
