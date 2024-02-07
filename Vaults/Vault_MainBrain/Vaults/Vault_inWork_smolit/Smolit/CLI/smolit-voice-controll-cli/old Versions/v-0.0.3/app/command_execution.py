
import subprocess

def execute_command(argument, command):
    full_command = f"sgpt {argument} {command}"
    try:
        output = subprocess.check_output(full_command, shell=True, stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return f"Fehler bei der Ausführung des Befehls: {e.output.decode()}"
