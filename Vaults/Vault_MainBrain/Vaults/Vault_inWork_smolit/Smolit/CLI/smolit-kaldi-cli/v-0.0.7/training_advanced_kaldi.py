
import subprocess
import logging

def run_kaldi_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        logging.info(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing {command}: {e}")
        raise

def prepare_data(dataset_path):
    # Advanced data preparation using Kaldi tools
    run_kaldi_command(f"utils/prepare_data.sh {dataset_path}")

def extract_features(data_directory):
    # Advanced feature extraction with detailed logging
    run_kaldi_command(f"steps/make_mfcc.sh --nj 4 {data_directory}")

def align_data(data_directory, model_dir, lang_dir):
    # Aligning data using Kaldi, crucial for training accurate models
    run_kaldi_command(f"steps/align_si.sh --nj 4 {data_directory} {lang_dir} {model_dir}")

def train_tri_model(data_directory, model_dir, lang_dir):
    # Training a triphone model, which is more advanced than a monophone model
    run_kaldi_command(f"steps/train_deltas.sh {data_directory} {lang_dir} {model_dir}")

def train_model(dataset_path, model_dir, lang_dir):
    logging.basicConfig(level=logging.INFO)
    prepare_data(dataset_path)
    extract_features(dataset_path)
    align_data(dataset_path, model_dir, lang_dir)
    train_tri_model(dataset_path, model_dir, lang_dir)
