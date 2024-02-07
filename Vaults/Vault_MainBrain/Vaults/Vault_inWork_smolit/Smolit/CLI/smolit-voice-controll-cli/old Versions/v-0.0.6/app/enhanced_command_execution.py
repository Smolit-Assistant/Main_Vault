
import subprocess

def execute_command(recognized_speech):
    # Parse the recognized speech to determine the command
    # This is a placeholder for the logic to parse and decide on the command
    command = recognized_speech  # Replace this with actual command parsing logic

    try:
        # Execute the command using subprocess
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return {"status": "success", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": f"Fehler bei der Ausführung des Befehls: {e.output.decode()}"}
