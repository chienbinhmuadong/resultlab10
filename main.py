from recognition import  Ears
from voice import voice
from commands import Command
import time


listener = Ears()
text_gen = listener.listen()
listener.stream.stop_stream()
voice.text_to_speech('Привет! Я голосовой ассистент!')
time.sleep(0.5)
listener.stream.start_stream()
for text in text_gen:
    print(text)
    listener.stream.stop_stream()
    Command(text)
    time.sleep(0.5)
    listener.stream.start_stream()