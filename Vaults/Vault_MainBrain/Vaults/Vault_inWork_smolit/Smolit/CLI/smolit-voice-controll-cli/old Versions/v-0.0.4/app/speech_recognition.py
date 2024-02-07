
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

    def listen(self):
        # Record audio from the microphone
        print("Listening...")
        with sd.InputStream(samplerate=self.sample_rate, channels=self.channels, dtype='float32') as stream:
            audio_data = np.array([], dtype='float32')
            while True:
                try:
                    data, overflowed = stream.read(self.buffer_size)
                    if overflowed:
                        logging.warning("Audio input overflowed")
                    
                    audio_data = np.append(audio_data, data)
                    if self.is_end_of_speech(audio_data):
                        break

                except Exception as e:
                    logging.error(f"Error during recording: {e}")
                    break

            if audio_data.size > 0:
                if self.decoder.decode(audio_data):
                    return self.decoder.get_decoded_string()
            return None

    def reset(self):
        # Reset the decoder for the next utterance
        self.decoder.reset()

    def is_end_of_speech(self, audio_data):
        # TODO: Implement a mechanism to detect the end of speech
        # Placeholder for end-of-speech detection logic
        pass
