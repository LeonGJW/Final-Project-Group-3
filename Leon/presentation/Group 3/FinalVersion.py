from __future__ import unicode_literals
from flask import Flask,request,Response,make_response,send_from_directory
import requests
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
import codecs
import sys
import os
reload(sys)
app = Flask(__name__)
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator

#Translate Part
language_translator = LanguageTranslator(
    username="90dc44bd-f01b-40f0-9448-58b2f6c2f751",
    password="JhiOqokZ6CfX")

inputsentence = raw_input("Please enter the sentence you want to translate: ")
desiredlanguageabb = raw_input("Please enter your target language from following options(de,en,ja,es,it,fr): ")

desireddic={'de':'German','en':'English',
            'es':'Spanish','ja':'Japanese',
           'it':'Italian','fr':'France'}
speak_language={'de':'de-DE_BirgitVoice','en':'en-GB_KateVoice',
                'es':'es-LA_SofiaVoice','ja':'ja-JP_EmiVoice',
                'it':'it-IT_FrancescaVoice','fr':'fr-FR_ReneeVoice'}

desiredlanguage=desireddic[desiredlanguageabb]
voice=speak_language[desiredlanguageabb]

language = language_translator.identify(inputsentence)
data = json.dumps(language, indent=2)

languages = language_translator.get_identifiable_languages()
ul=json.dumps(languages, indent=2)

with open('data.json', 'w+') as f:
    f.write(data)
    f.close

with open('data.json','r') as f:
    a = json.load(f)
    b = a['languages']
    c = b[0]['language']
    f.close

with open('choices.json', 'w+') as f:
    f.write(ul)
    f.close

with open('choices.json', 'r') as f:
    aa = json.load(f)
    bb = aa['languages']
    for i in range(0,61):
        cc = bb[i]['name']
        if cc == desiredlanguage:
            dd = bb[i]['language']
        else:
            i += 1
    for i in range(0,61):
        cc = bb[i]['language']
        if cc == c:
            ee = bb[i]['name']
    else:
        i += 1
    f.close

print("The language you typed in is: " + ee)

translation = language_translator.translate(
    text=inputsentence,
    source=c,
    target=dd)
result = json.dumps(translation, indent=2)

with open('result.json', 'w+') as f:
    f.write(result)
    f.close
    print("Translation result is" + result)

#---------------------------------------------------------------------------------------#
#--------------------------------------Text to Speech Part------------------------------#
#---------------------------------------------------------------------------------------#
sys.setdefaultencoding('utf8')
username='925d730b-e6ec-48fc-93fb-0ed640400f76',
password='VHEQdxsP7H1O'
text = 'hello Australia'
say_this = result
#-----------------------Text To Speech API credentials go here--------------------------#
text_to_speech = TextToSpeechV1(username='925d730b-e6ec-48fc-93fb-0ed640400f76', password='VHEQdxsP7H1O')
#---------------------------------------------------------------------------------------#




s=json.dumps(speak_language, indent=2)

with open('languages.json', 'w+') as f:
    f.write(s)
"""
with open('languages.json','r') as f:
    aaa = json.load(f)
    for i in range(0,5):
        if aaa[i] == dd:
            bbb = i
        else:
            i += 1
"""

fn = 'output.mp3'
with open(join(dirname(__file__), '/Users/guojiawei/Leon/presentation/audio/'+fn), 'wb') as audio_file:
    audio_file.write(text_to_speech.synthesize(say_this,voice=voice))
