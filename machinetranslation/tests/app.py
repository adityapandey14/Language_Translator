from flask import Flask, render_template, request
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("apikey")
url = os.getenv("url")

authenticator= IAMAuthenticator(apikey)
lt=LanguageTranslatorV3(version='2018-05-01' , authenticator=authenticator)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    input_text = request.form['inputText']
    translation_text = ''
    if request.form['translateDirection'] == 'en-fr':
        if input_text:
            translation_text = englishToFrench(input_text)
    elif request.form['translateDirection'] == 'fr-en':
        if input_text:
            translation_text = frenchToEnglish(input_text)
    return render_template('index.html', translation_text=translation_text)

def englishToFrench(englishText):
    lt.set_service_url(url)
    if englishText is None:
        return None
    translation = lt.translate(
        text=englishText,
        model_id='en-fr').get_result()
    translation=translation['translations'][0]['translation']
    return translation

def frenchToEnglish(frenchText):
    lt.set_service_url(url)
    if frenchText is None:
        return None
    translation = lt.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    translation=translation['translations'][0]['translation']
    return translation

if __name__ == '__main__':
    app.run(debug=True)
