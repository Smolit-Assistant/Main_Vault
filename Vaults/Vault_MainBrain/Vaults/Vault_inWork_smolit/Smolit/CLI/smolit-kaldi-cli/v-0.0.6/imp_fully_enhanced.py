
import subprocess
import logging

def export_model_to_format(model_path, export_format, export_dir):
    # Exporting the model to a specified format
    # This function allows for the conversion of the trained model into different formats for deployment
    try:
        subprocess.run(f"utils/export_model.sh {model_path} {export_format} {export_dir}", shell=True, check=True)
        logging.info(f"Model exported in {export_format} format to {export_dir}.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error in model export: {e}")
        raise

def export_model(model_path, export_format, export_dir):
    # Main function to handle model export
    logging.basicConfig(level=logging.INFO)
    export_model_to_format(model_path, export_format, export_dir)
