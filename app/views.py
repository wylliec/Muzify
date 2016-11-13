from flask import render_template, request, jsonify
from app import app
from app.watson import analyze_tone, get_sentiments, speech_text 
from app.wav_combine import combine_waves, read_wav
from app.playlists import play_song
from app.mood_analysis import get_max_emotion
import json

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/speech-to-tone')
def speech_to_tone():
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
    #print('i got it')
    wav_fname = request.form['fname']
    wav_upload = request.files['data']
    #print(wav_fname)
    #print(wav_upload)
    #wav_upload.save('app/static/record.wav')
    old_wav = read_wav('app/static/record.wav')
    new_wav = read_wav(wav_upload)
    combine_waves(old_wav, new_wav, 'app/static/record.wav')
    text = speech_text()
    sentiments = get_sentiments(analyze_tone(text))
    d = {}
    d['text'] = text
    d['mood'] = get_max_emotion(sentiments)
    d['preview_url'] = play_song(d['mood'])
    return jsonify(**d)

@app.route('/upload', methods=['DELETE'])
def delete():
    overwrite = open('app/static/empty.wav', 'rb')
    delet_this = open('app/static/record.wav', 'wb')
    delet_this.write(overwrite.read())
    return 'successful deletion'
