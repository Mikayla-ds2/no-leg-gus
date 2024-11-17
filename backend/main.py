from flask import Flask, jsonify, request
from flask_cors import CORS

import random

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def home():
     # Get the JSON data from the request
     data = request.json
     msgtxt = data.get('msgtxt','') # Extract msgtxt, default to empt string if not present 

     reply = ''
     
     if 'earth' in msgtxt:
          reply = 'Earth has a radius of 3,959 miles, a volume of 259.9 billion cubic miles, with a single moon, and a mean temperature of 59 degrees Fahrenheit.'
     elif 'saturn' in msgtxt:
          reply = "Saturn has a radius of 36,184 miles, a volume of 263,846 billion cubic miles, with 146 moons, and a mean temperature of -220 degrees Fahrenheit."
     elif 'venus' in msgtxt:
          reply = "Venus has a radius of 3,760 miles, a volume of 222.9 billion cubic miles, with 0 moons, and a mean temperature of 867 degrees Fahrenheit."
     elif 'mars' in msgtxt:
          reply = "Mars has a radius of 2,106 miles, a volume of 39.2 billion cubic miles, with 2 moons, and a mean temperature of -85 degrees Fahrenheit."
     elif 'mercury' in msgtxt:
          reply = "Mercury has a radius of 1,516 miles, a volume of 14.6 billion cubic miles, with 0 moons, and a mean temperature of 333 degrees Fahrenheit."
     elif 'jupiter' in msgtxt:
          reply = "Jupiter has a radius of 43,441 miles, a volume of 343,345 billion cubic miles, with 95 moons, and a mean temperature of -166 degrees Fahrenheit." 
     elif 'neptune' in msgtxt:
          reply = "Neptune has a radius of 15,299 miles, a volume of 57,754 billion cubic miles, with 16 moons, and a mean temperature of -330 degrees Fahrenheit."
     elif 'uranus' in msgtxt:
          reply = "Uranus has a radius of 15,759 miles, a volume of 65,394 billion cubic miles, with 28 moons, and a mean temperature of -320 degrees Fahrenheit."     
     else:
          reply = "I'm sorry, I don't understand. Please ask me about the planets in the solar system."
     #Process the msgtxt or respond accordingly
     resp = {
          'gusReply': reply
     }
     return jsonify(resp)

if __name__ == '__main__':
     app.run(debug=True)
     