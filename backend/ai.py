from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dictionary legend: { Planet : [temp (F), radius (mi), volume (billion mi^3), # of moons ]}
d = {
    'Mercury' : [333, 1516, 14.6, 0], 
    'Venus' : [867, 3760, 222.9, 0],
    'Mars' : [-85, 2106, 39.2, 2], 
    'Earth' : [59, 3959, 259.9, 1],
    'Jupiter' : [-166, 43441, 343345, 95],
    'Saturn' : [-220, 36184, 263846, 146], 
    'Uranus' : [-320, 15759, 65394, 28], 
    'Neptune' : [-330, 15299, 57754, 16]
}


# if temp < 0:
    # loop through dictionary list[0] and adds planet name to potential planet list