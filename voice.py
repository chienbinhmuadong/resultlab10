from vosk_tts import Model, Synth
from playsound import playsound
import os
import time


class Voice:
    def __init__(self):
        model = Model(model_name='vosk-model-tts-ru-0.6-multi')
        self.synth = Synth(model)
        self.speaker= 1


    def text_to_speech(self, text="добрый день!"):
        res = self.synth.synth(text,
                         "out.wav",
                         speaker_id = self.speaker
                         ) 
        playsound("./"+"out.wav")


    def set_voice(self, speaker):
        self.speaker = speaker

voice = Voice()


# if __name__ == "__main__":
#       voice = Voice()
#       voice.text_to_speech()     