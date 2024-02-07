
import subprocess
import logging

def run_kaldi_command(command, description):
    # Running Kaldi commands with advanced features
    try:
        subprocess.run(command, shell=True, check=True)
        logging.info(f"Successfully completed: {description}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error during {description}: {e}")
        raise

def specialized_decode_model(model_dir, testset_path, decode_dir):
    # Advanced decoding using specialized Kaldi techniques
    run_kaldi_command(f"steps/specialized_decode.sh {model_dir} {testset_path} {decode_dir}", "specialized model decoding")

def detailed_model_evaluation(decode_dir):
    # Detailed evaluation of the model's performance with advanced metrics
    run_kaldi_command(f"steps/detailed_score_kaldi.sh {decode_dir}", "detailed model evaluation")

def test_and_refine_model(testset_path, model_dir, decode_dir):
    logging.basicConfig(level=logging.INFO)
    specialized_decode_model(model_dir, testset_path, decode_dir)
    detailed_model_evaluation(decode_dir)
