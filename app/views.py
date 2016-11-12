from flask import render_template
from app import app
from app.watson import analyze_tone, get_sentiments, speech_text 
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

@app.route('/upload')
def upload():
    return render_template('exampleRecording.html')
