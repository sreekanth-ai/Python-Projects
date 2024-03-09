import pyttsx3


def onStart():
    print('starting')


def onWord(name, location, length):
    print('word', name, location, length)


def onEnd(name, completed):
    print('finishing', name, completed)


engine = pyttsx3.init()

engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)

sen = 'Myself sreekanth I am very much Interested in Data science and Machine Learning'

engine.say(sen)
engine.runAndWait()
