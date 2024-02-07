
import time
import subprocess
import logging

def run_kaldi_command(command):
    # Function to run a Kaldi command with robust error handling
    try:
        subprocess.run(command, shell=True, check=True)
        logging.info(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing {command}: {e}")
        raise

def retrain_model(model_dir, new_data_path, lang_dir):
    # Retraining the model with Kaldi using the newly collected data
    run_kaldi_command(f"steps/train_deltas.sh {new_data_path} {lang_dir} {model_dir}")

def continuous_improvement(data_collection_function, retrain_interval, model_dir, lang_dir):
    logging.basicConfig(level=logging.INFO)
    while True:
        try:
            new_data_path = data_collection_function()
            retrain_model(model_dir, new_data_path, lang_dir)
            time.sleep(retrain_interval)
        except Exception as e:
            logging.error(f"Error in continuous improvement loop: {e}")
            time.sleep(60) # Wait a minute before retrying
