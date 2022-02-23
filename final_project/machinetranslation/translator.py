import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#authenticator = IAMAuthenticator('{apikey}')
authenticator = IAMAuthenticator('DZhHkbmm3Z3taQQgfkL0lXj1rM07m8JALBxoIY2Vc9YP')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

#language_translator.set_service_url('{url}')
language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/dd831624-e143-4d8c-8493-c8cafb04c8f1')


def english_to_french(english_text):
    #write the code here
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text =translation['translations']
    return french_text

def french_to_english(french_text):
    #write the code here
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text =translation['translations']
    return english_text