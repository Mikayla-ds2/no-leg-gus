from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
     # Get the JSON data from the request
     data = request.json
     msgtxt = data.get('msgtxt','') # Extract msgtxt, default to empt string if not present 

     #Process the msgtxt or respond accordingly
     resp = {
          'gusReply': f'You said: {msgtxt}'
     }

     return jsonify(resp)

if __name__ == '__main__':
     app.run(debug=True)