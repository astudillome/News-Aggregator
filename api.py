import time
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import json

app = Flask(__name__)

@app.route('/time')
def get_current_time():
  return { 'time': time.time()}

@app.route('/nytresults', methods=['GET'])
def get_articles():
  data = requests.get("https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&api-key=0XvEh8pQ6usIUskmlliZNvlebumtyLml").json()
  return {'nyt_data': data}
