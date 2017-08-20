from __future__ import unicode_literals
from flask import Flask,request,Response,make_response,send_from_directory
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
import codecs
import sys
reload(sys)
app = Flask(__name__)
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator

#Chen Shen
#Translator identification
language_translator = LanguageTranslator(
    username="90dc44bd-f01b-40f0-9448-58b2f6c2f751",
    password="JhiOqokZ6CfX")

#Ask for user input
inputsentence = raw_input("Please enter the sentence you want to translate: " + '\n')
desiredlanguage = raw_input("Please enter your target language: " + '\n')

#Identify the language of the input sentence and export the data to json file
language = language_translator.identify(inputsentence)
data = json.dumps(language, indent=2)

#Get the list of available languages
languages = language_translator.get_identifiable_languages()
ul=json.dumps(languages, indent=2)

#json file's output
with open('data.json', 'w+') as f:
    f.write(data)
    f.close

#Select the most possible language automatically
with open('data.json','r') as f:
    a = json.load(f)
    b = a['languages']
    c = b[0]['language']
    f.close

#List of available languages
with open('choices.json', 'w+') as f:
    f.write(ul)
    f.close

#Compare and reach a decision
with open('choices.json', 'r') as f:
    aa = json.load(f)
    bb = aa['languages']
    for i in range(0,61):
        cc = bb[i]['name']
        if cc == desiredlanguage:
            dd = bb[i]['language']
            ff = bb[i]['name']
        else:
            i += 1
    for i in range(0,61):
        cc = bb[i]['language']
        if cc == c:
            ee = bb[i]['name']
    else:
        i += 1
    f.close

print("The language you typed in is: " + ee + '\n')

#Use the IBM Watson translate service
translation = language_translator.translate(
    text=inputsentence,
    source=c,
    target=dd)
result = json.dumps(translation, indent=2, ensure_ascii=False)
print("Translation result is " + '\n' + result )

#Jiawei Guo:TEXT-TO-SPEECH
sys.setdefaultencoding('utf8')
username='925d730b-e6ec-48fc-93fb-0ed640400f76',
password='VHEQdxsP7H1O'
text = 'hello Australia'
voice = 'en-GB_KateVoice'
accept = ''
say_this = result
#-----------------------Text To Speech API credentials go here--------------------------#
text_to_speech = TextToSpeechV1(username='925d730b-e6ec-48fc-93fb-0ed640400f76',password='VHEQdxsP7H1O')
#---------------------------------------------------------------------------------------#

#-----------------------Do You wish to see the latest API summary-----------------------#
#set to yes or no
#---------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------#
#---------------------------extract the information from the texttospeech API       ----#
#---------------------------------------------------------------------------------------#

def see_api_list():

    x = text_to_speech.voices()
    all_voices_in_dictionary = x['voices']
    name_voices = []
    y = len(all_voices_in_dictionary)
    i = 0
    for i in range (y):
        record = all_voices_in_dictionary[i]
        for key in record.keys():
            try:

                g = record[key]
                str(g).strip( unicode( codecs.BOM_UTF8, "utf8" ) )
                g = g.decode('utf-8')
            except AttributeError:
                str(g).strip( unicode( codecs.BOM_UTF8, "utf8" ) )
                g = str(g)
            except UnicodeEncodeError:
                g.encode('utf-8','ignore')
            if key == 'name':
                name_voices.append(g.encode('utf-8'))
    return(name_voices)

if __name__ == "__main__":
    name_voices = see_api_list()

#Tianyi Mao:File output
speak_language={'de-DE':'de-DE_BirgitVoice','en-GB':'en-GB_KateVoice',
                'en-US':'en-US_AllisonVoice','es-ES':'es-ES_LauraVoice',
                'es-LA':'es-LA_SofiaVoice','ja-JP':'ja-JP_EmiVoice',
                'it-IT':'it-IT_FrancescaVoice','fr-FR':'fr-FR_ReneeVoice'}
if dd == 'de':
    voice = 'de-DE_BirgitVoice'

if dd == 'en':
    voice = 'en-GB_KateVoice'
    voice1 = 'en-US_AllisonVoice'

if dd == 'es':
    voice = 'es-ES_LauraVoice'
    voice1 = 'es-LA_SofiaVoice'

if dd == 'ja':
    voice = 'ja-JP_EmiVoice'

if dd == 'it':
    voice = 'it-IT_FrancescaVoice'

if dd == 'fr':
    voice = 'fr-FR_ReneeVoice'

fn = 'output_'+ ff +'.mp3'
with open(join(dirname(__file__), '/Users/Chen/Desktop/FinalProject/'+fn), 'wb') as audio_file:
    audio_file.write(text_to_speech.synthesize(say_this,voice=voice))

try:
    voice=voice1
    fn1 = 'output1_'+ ff +'.mp3'
    with open(join(dirname(__file__), '/Users/Chen/Desktop/FinalProject/'+fn1), 'wb') as audio_file:
        audio_file.write(text_to_speech.synthesize(say_this,voice=voice1))
except:
    pass
