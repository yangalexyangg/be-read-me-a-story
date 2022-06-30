from flask import Flask
from flask import request
from firebase_admin import db
from flask_cors import cross_origin
from db.connection import app
import uuid
import time

app = Flask(__name__)

@app.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/stories', methods=['POST', 'GET'])
@cross_origin()
def stories():
    if request.method == 'GET':
        stories = db.reference("/stories")
        return stories.get()

    if request.method == "POST":
        stories = db.reference("stories/" + str(uuid.uuid4()))
        res = stories.set({
            "title": "The Twelve Princesses",
            "created_by": "andy@email.com",
            "created_at": int(time.time()),
            "cover": "gs:/path/to/firebase/image.jpg",
            "chapters": [
                {
                    "created_by": "andy@email.com",
                    "chapter_src": "gs:/path/to/recording/file.ogg",
                    "played": False
                }
            ],
            "families": {
                "fid_0": True,
                "fid_1": True
            }
        })
