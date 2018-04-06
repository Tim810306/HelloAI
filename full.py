# coding:utf-8
import speech_recognition

def listenTo():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    return r.recognize_google(audio, language='zh-TW')

import tempfile
from gtts import gTTS
from pygame import mixer
mixer.init()

def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang='zh')
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()

#speak('大家好')

#speak(listenTo())

#
m = speech_recognition.Microphone()
m.CHUNK = 8192 # increased by a factor of 8
with m as source:
    pass # do the usual stuff here
qa = {
   '你今天好嗎': '我很好',
   '你好美'    : '你也很帥',
   '誰是世界上最帥的人' : '當然是你壓'
 }


speak(qa.get(listenTo(), '我現在還在學習, 等我變聰明以後, 我再回答你'))
