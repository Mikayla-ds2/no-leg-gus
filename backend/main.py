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
          reply = 'Earth has a '
          
     if 'hi' in msgtxt:
          reply = "Hello!"

     #Process the msgtxt or respond accordingly
     resp = {
          #'gusReply': f'Hello: {msgtxt}'
          'gusReply': reply
     }
     return jsonify(resp)

if __name__ == '__main__':
     app.run(debug=True)
     