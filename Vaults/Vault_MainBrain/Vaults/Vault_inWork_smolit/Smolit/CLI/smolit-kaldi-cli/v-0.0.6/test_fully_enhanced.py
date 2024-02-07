
import subprocess
import logging

def decode_model(model_dir, testset_path, decode_dir):
    # Decoding the model with a test dataset using Kaldi
    # This function handles the process of using the trained model to decode a test dataset
    try:
        subprocess.run(f"steps/decode.sh --nj 4 {model_dir} {testset_path} {decode_dir}", shell=True, check=True)
        logging.info("Decoding completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error in decoding: {e}")
        raise

def evaluate_model(decode_dir):
    # Evaluating the model's performance
    # This involves calculating various metrics like word error rate (WER)
    try:
        subprocess.run(f"steps/score_kaldi.sh {decode_dir}", shell=True, check=True)
        logging.info("Model evaluation completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error in model evaluation: {e}")
        raise

def test_and_refine_model(testset_path, model_dir, decode_dir):
    # Main function to handle testing and refining the model
    logging.basicConfig(level=logging.INFO)
    decode_model(model_dir, testset_path, decode_dir)
    evaluate_model(decode_dir)
