
import argparse
import os
import subprocess
import logging
from training_specialized_kaldi import train_model
from test_specialized_kaldi import test_and_refine_model
from loop_specialized_kaldi import continuous_improvement, data_collection_function_mic, data_collection_function_stream, data_collection_function_file
from imp_specialized_kaldi import export_model

def new_model(username, model_dir):
    user_dir = f"{username}/profile"
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)
    print(f"New model for user {username} created at {user_dir}")

    # Initialize model directory
    os.makedirs(model_dir, exist_ok=True)

def run_in_debug_mode():
    logging.basicConfig(level=logging.DEBUG)
    print("Running in debug mode...")

def main():
    parser = argparse.ArgumentParser(description='smolit CLI tool for personalized language model generation.')
    parser.add_argument('--new-model', help='Create a new user profile and project directory', type=str)
    parser.add_argument('--debug', help='Run in debug mode', action='store_true')
    parser.add_argument('--train', help='Train a new model', action='store_true')
    parser.add_argument('--test', help='Test and refine the model', action='store_true')
    parser.add_argument('--loop', help='Continuously improve the model', action='store_true')
    parser.add_argument('--stream', help='Collect data from a live stream', type=str, default=None)
    parser.add_argument('--file', help='Collect data from a file', type=str, default=None)
    parser.add_argument('--export', help='Export the model', action='store_true')
    args = parser.parse_args()

    if args.new_model:
        new_model(args.new_model, "path/to/model/directory")

    if args.debug:
        run_in_debug_mode()

    if args.train:
        train_model("path/to/training/dataset", "path/to/model/directory", "path/to/lang/directory")

    if args.test:
        test_and_refine_model("path/to/test/dataset", "path/to/model/directory", "path/to/decode/directory")

    if args.loop:
        data_collection_function = None
        if args.stream:
            data_collection_function = lambda: data_collection_function_stream(args.stream)
        elif args.file:
            data_collection_function = lambda: data_collection_function_file(args.file)
        elif not args.stream and not args.file:
            data_collection_function = data_collection_function_mic

        if data_collection_function:
            continuous_improvement(data_collection_function, 3600, "path/to/model/directory", "path/to/lang/directory")
        else:
            print("No valid data collection method specified for loop.")

    if args.export:
        export_model("path/to/model", "desired_format", "path/to/export/directory")

if __name__ == "__main__":
    main()
