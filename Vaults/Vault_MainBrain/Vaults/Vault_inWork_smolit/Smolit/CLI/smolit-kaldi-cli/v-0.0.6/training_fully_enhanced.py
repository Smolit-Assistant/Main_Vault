
import subprocess
import logging

def prepare_data(dataset_path):
    # Preparing the data using Kaldi utilities
    # This includes formatting the data directory and validating data files
    try:
        subprocess.run(f"utils/prepare_data.sh {dataset_path}", shell=True, check=True)
        logging.info("Data preparation completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error in data preparation: {e}")
        raise

def extract_features(data_directory):
    # Extracting MFCC features using Kaldi
    # Feature extraction is a crucial step in preparing audio data for training
    try:
        subprocess.run(f"steps/make_mfcc.sh --nj 4 {data_directory}", shell=True, check=True)
        logging.info("Feature extraction completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error in feature extraction: {e}")
        raise

def train_mono_model(data_directory, model_dir):
    # Training a monophone model using Kaldi
    # Monophone models are an initial step in training more complex models
    try:
        subprocess.run(f"steps/train_mono.sh --nj 4 --cmd run.pl {data_directory} {model_dir}", shell=True, check=True)
        logging.info("Mono model training completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error in mono model training: {e}")
        raise

def train_model(dataset_path, model_dir):
    # Main function to handle the training process
    logging.basicConfig(level=logging.INFO)
    prepare_data(dataset_path)
    extract_features(dataset_path)
    train_mono_model(dataset_path, model_dir)
