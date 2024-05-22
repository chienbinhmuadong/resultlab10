from voice import voice
import handlers


COMMANDS = [
    {'id': 0, 'text': 'создать', 'handler': handlers.create},
    {'id': 1, 'text': 'имя', 'handler': handlers.name},
    {'id': 2, 'text': 'страна', 'handler': handlers.country},
    {'id': 3, 'text': 'анкета', 'handler': handlers.document},
    {'id': 4, 'text': 'сохранить', 'handler': handlers.save}
] 

ACTIVATION = 'запуск'


class Command:

    def __init__(self, text):
        self.text = text
        self.map()
        
    def map(self):
        if self.text.startswith(ACTIVATION):
            self.text = self.text.replace(ACTIVATION, '').strip()
            if self.text.startswith('создать'):
                user = handlers.create()
                self.text = self.text.replace('создать', '').strip()
                for cmd in COMMANDS:
                    if self.text.startswith(cmd['text']):
                        self.run(cmd, user)
                        return True
            else:
                voice.text_to_speech("вам придётся создать ползователя")
        else:
            voice.text_to_speech('Я не знаю такой команды, простите!')
           

    def run(self, cmd, user):
        handler = cmd['handler']
        handler(user)
        