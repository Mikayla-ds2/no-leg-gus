from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
     resp = {
          'gusReply': 'hi there buddy'
     }

     return jsonify(resp)

if __name__ == '__main__':
     app.run(debug=True)