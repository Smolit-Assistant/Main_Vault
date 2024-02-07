
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
            logging.error(f"Error initializing Kaldi model: {e}")
            raise

    def stream_from_microphone(self, process_func):
        def callback(indata, frames, time, status):
            if status:
                logging.warning(status)
            audio = np.frombuffer(indata, dtype=np.int16)
            process_func(audio)

        with sd.InputStream(samplerate=self.sample_rate, channels=self.channels, callback=callback):
            print("Listening, press Ctrl+C to stop.")
            while True:
                pass

    def recognize_speech(self, audio):
        try:
            # Decoding the speech
            self.decoder.decode_wav_data(audio.tobytes())
            text = self.decoder.get_decoded_string()
            return text
        except Exception as e:
            logging.error(f"Error in speech recognition: {e}")
            return None

# Example usage
if __name__ == "__main__":
    sr = SpeechRecognition("path/to/model")
    sr.stream_from_microphone(sr.recognize_speech)
