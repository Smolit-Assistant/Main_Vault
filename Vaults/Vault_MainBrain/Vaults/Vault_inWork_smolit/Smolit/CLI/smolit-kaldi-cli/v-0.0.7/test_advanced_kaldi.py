
import subprocess
import logging

def run_kaldi_command(command):
    # Reusable function to run a Kaldi command with error handling
    try:
        subprocess.run(command, shell=True, check=True)
        logging.info(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing {command}: {e}")
        raise

def decode_model(model_dir, testset_path, decode_dir):
    # Advanced model decoding using Kaldi
    run_kaldi_command(f"steps/decode.sh --nj 4 {model_dir} {testset_path} {decode_dir}")

def evaluate_model(decode_dir):
    # Advanced evaluation of the model's performance
    run_kaldi_command(f"steps/score_kaldi.sh {decode_dir}")

def test_and_refine_model(testset_path, model_dir, decode_dir):
    logging.basicConfig(level=logging.INFO)
    decode_model(model_dir, testset_path, decode_dir)
    evaluate_model(decode_dir)
