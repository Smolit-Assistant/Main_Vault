
import subprocess
import logging

def run_kaldi_command(command, description):
    # Advanced model export functionality using Kaldi
    try:
        subprocess.run(command, shell=True, check=True)
        logging.info(f"Successfully completed: {description}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error during {description}: {e}")
        raise

def export_model_to_advanced_format(model_path, export_format, export_dir):
    # Exporting the model into various advanced formats
    run_kaldi_command(f"utils/advanced_export_model.sh {model_path} {export_format} {export_dir}", "advanced model export")

def export_model(model_path, export_format, export_dir):
    logging.basicConfig(level=logging.INFO)
    export_model_to_advanced_format(model_path, export_format, export_dir)
