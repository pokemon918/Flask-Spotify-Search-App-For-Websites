import os
import sys
import json
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')

def download():
    key = request.args.get('key')
    main_dict={}
    if key=="search":
        search = request.args.get('search')
        song=request.args.get('song')
        artist=request.args.get('artist')
        button=request.args.get('button')
        spotify_code=request.args.get('spotify_code')
        timer=request.args.get('timer')
        my_dict=dict()
        my_dict["id"]=500
        my_dict["song"]=song
        my_dict["artist"]=artist
        my_dict["button"]=button
        my_dict["spotify_code"]=spotify_code
        my_dict["timer"]=timer
        main_dict["id"]=my_dict
        return json.dumps(main_dict)

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

    
application=app
