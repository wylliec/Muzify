from flask import render_template, request
from app import app
from app.watson import analyze_tone, get_sentiments, speech_text 
from app.wav_combine import combine_waves, read_wav
import json

@app.route('/')
@app.route('/index')
def index():
    text = analyze_tone(speech_text())
    sentiments = str(get_sentiments(text))
    str_sentiments = str(sentiments) 
    return render_template('pre.html', text=sentiments)

@app.route('/tone')
def tone():
    text = 'eecs for lyfe yo'
    tone = analyze_tone(text)
    str_json = json.dumps(tone, indent=2)
    return render_template('pre.html', text=str_json)

@app.route('/speech')
def speech():
    text = speech_text()
    str_json = json.dumps(text, indent=2)
    return render_template('pre.html', text=str_json)

@app.route('/record')
def record():
    return render_template('exampleRecording.html')

@app.route('/upload', methods=['POST'])
def upload():
    print('i got it')
    wav_fname = request.form['fname']
    wav_upload = request.files['data']
    print(wav_fname)
    print(wav_upload)
    old_wav = read_wav('app/static/speech.wav')
    new_wav = read_wav(wav_upload)
    combine_waves(old_wav, new_wav, 'app/static/speech.wav')
    return 'successful upload'
