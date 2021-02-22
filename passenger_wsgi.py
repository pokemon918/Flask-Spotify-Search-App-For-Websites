import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, request, render_template, redirect, url_for
import json

project_root = os.path.dirname(os.path.realpath('__file__'))
template_path = os.path.join(project_root, 'app/templates')
static_path = os.path.join(project_root, 'app/static')
app = Flask(__name__, template_folder=template_path, static_folder=static_path)

class spotify_data():
    def __init__(self,name):
        os.environ['SPOTIPY_CLIENT_ID'] = 'b0f9df05edf246f6b7c4bcf0aa500232'  
        os.environ['SPOTIPY_CLIENT_SECRET'] = '8c344c1fc91f4842bf108829aeeeeafd'
        search_str = name
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        self.result = sp.search(search_str,5)
        self.veri=dict()
        for i in range(5):
            my_dict={}
            my_dict["id"]=self.result['tracks']['items'][i]['id']
            my_dict["cover_img"]=self.result['tracks']['items'][i]['album']['images'][0]['url']
            my_dict["name"]=self.result['tracks']['items'][i]['name']
            my_dict["artist"]=self.result['tracks']['items'][i]['album']['artists'][0]['name']
            self.veri[my_dict["id"]] = my_dict
            
@app.route('/')
def hello():
    key = request.args.get('key')
    if key=="search":
        search = request.args.get('search')
        yilmaz=spotify_data(search)
        return json.dumps(yilmaz.veri)
    elif key=="info":
        return os.path.join(project_root, 'app/static')
    elif key=="static":
        path = os.path.join(project_root, 'app/static', request.args.get('path'))
        return  open(path,"rb").read()
@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
    
application = app
