
import subprocess
import logging

def run_kaldi_command(command):
    # Function to handle model exporting with Kaldi
    try:
        subprocess.run(command, shell=True, check=True)
        logging.info(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing {command}: {e}")
        raise

def export_model_to_format(model_path, export_format, export_dir):
    # Exporting the model into different formats for deployment
    run_kaldi_command(f"utils/export_model.sh {model_path} {export_format} {export_dir}")

def export_model(model_path, export_format, export_dir):
    logging.basicConfig(level=logging.INFO)
    export_model_to_format(model_path, export_format, export_dir)
