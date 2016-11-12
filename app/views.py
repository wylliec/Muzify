from flask import render_template
from app import app
from app.watson import analyze_tone, speech_text
import json

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/tone')
def tone():
    text = 'eecs for lyfe yo'
    tone = analyze_tone(text)
    str_json = json.dumps(tone, indent=2)
    return render_template('tone.html', text=str_json)

@app.route('/speech')
def speech():
    text = speech_text()
    str_json = json.dumps(text, indent=2)
    return render_template('tone.html', text=str_json)
