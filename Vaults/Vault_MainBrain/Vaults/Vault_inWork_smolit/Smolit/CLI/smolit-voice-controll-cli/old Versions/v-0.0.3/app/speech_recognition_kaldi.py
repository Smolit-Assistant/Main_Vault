
import kaldi_io
from kaldi.asr import Nnet3OnlineModel, Nnet3OnlineDecoder
import sounddevice as sd
import numpy as np

class SpeechRecognition:
    def __init__(self, model_dir):
        # Initialize Kaldi model and decoder
        self.model = Nnet3OnlineModel.from_dir(model_dir)
        self.decoder = Nnet3OnlineDecoder(self.model)

    def listen(self):
        # Record audio from the microphone
        print("Listening...")
        with sd.InputStream(samplerate=16000, channels=1, dtype='float32') as stream:
            while True:
                data, overflowed = stream.read(4096)
                if overflowed:
                    print("Warning: audio input overflowed")

                if self.decoder.decode(data):
                    yield self.decoder.get_decoded_string()

    def reset(self):
        # Reset the decoder for the next utterance
        self.decoder.reset()
