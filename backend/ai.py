from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

planets = {
    "Mercury" : {
        "characteristics": [1,0,1,0], #1: Yes, 0: No
        "questions": [ 
            "is it the smallest planet?",       
            "is the atmosphere very thin?",
            "is temperature extreme vartions throughout the day?",
            "would the atmosphere be rough/losts of craters?"
        ]
    },
    "Venus": {
        "characteristics": [1,0,0,0],
        "questions": [
            "i"
        ]
    }
}