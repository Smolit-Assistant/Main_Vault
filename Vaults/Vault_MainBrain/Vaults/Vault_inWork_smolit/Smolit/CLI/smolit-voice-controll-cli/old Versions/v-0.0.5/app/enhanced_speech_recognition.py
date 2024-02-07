
import kaldi_io
from kaldi.asr import Nnet3OnlineModel, Nnet3OnlineDecoder
import sounddevice as sd
import numpy as np
import logging

class SpeechRecognition:
    def __init__(self, model_dir, sample_rate=16000, channels=1, buffer_size=4096):
        self.sample_rate = sample_rate
        self.channels = channels
        self.buffer_size = buffer_size

        try:
            # Initialize Kaldi model and decoder
            self.model = Nnet3OnlineModel.from_dir(model_dir)
            self.decoder = Nnet3OnlineDecoder(self.model)
        except Exception as e:
            logging.error(f"Failed to initialize Kaldi model: {e}")
            raise

    def continuous_listen(self, on_recognized):
        with sd.InputStream(callback=self.audio_callback, channels=self.channels, samplerate=self.sample_rate):
            logging.info("Listening...")
            while True:
                # This loop will keep the stream open and listening continuously
                pass

    def audio_callback(self, indata, frames, time, status):
        if status:
            logging.warning(f"Stream status: {status}")

        try:
            # Convert audio input to suitable format for Kaldi
            audio_data = np.frombuffer(indata, dtype=np.float32)
            if self.decoder.accept_waveform(audio_data):
                # Process recognized speech
                recognized_text = self.decoder.decode()
                on_recognized(recognized_text)
        except Exception as e:
            logging.error(f"Error in audio processing: {e}")

# Example usage
if __name__ == "__main__":
    def print_recognized_text(text):
        print(f"Recognized: {text}")

    try:
        speech_recognition = SpeechRecognition(model_dir="path/to/kaldi/model")
        speech_recognition.continuous_listen(print_recognized_text)
    except Exception as e:
        logging.error(f"Speech recognition initialization failed: {e}")
