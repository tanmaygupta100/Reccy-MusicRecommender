from flask import Flask, request
import spotipy.util as util

app = Flask(__name__)

@app.route('/callback')
def callback():
    # Handle the Spotify callback here
    data = request.get_json()

    # Print the received data
    print("Received JSON data:", data)

    return "Data received successfully!"

if __name__ == '__main__':
    app.run(port=8888)
