#Reccy, BETA
#This 1.0 version is only text-based, using the terminal.

# Import necessary modules from Spotipy library:
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util


# Set up your Spotify API credentials:
client_id = '1234' # Your Spotify API client ID
client_secret = '1234' # Your Spotify API client secret
redirect_uri = 'http://localhost:8888/callback' # Redirect URI for user authorization

# Set up user credentials: (replace 'your_username' with your Spotify username)
username = 'your_username' # Initialize username as default, prompt for personalization later.
scope = 'user-library-read user-read-private user-read-playback-state user-modify-playback-state playlist-modify-public'

# Get a user token for authentication:
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

# Check if the token was successfully obtained:
if token:
    sp = spotipy.Spotify(auth=token) # Create a Spotify object with the authenticated token.
else:
    print("Can't get token for", username)

# Function to get a track URI by name:
def get_track_uri(track_name):
    # Use the Spotify API to search for a track by name
    results = sp.search(q=track_name, type='track', limit=1)
    items = results['tracks']['items']

    # Check if any tracks were found
    if items:
        # Return the URI of the first track found
        return items[0]['uri']
    else:
        # Print a message if no track was found
        print(f"No track found with the name: {track_name}")
        return None

# Function to get track recommendations based on a track URI:
def get_recommendations(track_uri):
    # Use the Spotify API to get track recommendations based on a seed track
    results = sp.recommendations(seed_tracks=[track_uri], limit=5)
    return results['tracks']

# Example usage:
song_name = input("Enter the name of the song: ")
track_uri = get_track_uri(song_name)

# Check if a track URI was obtained:
if track_uri:
    # Get recommendations based on the entered track
    recommendations = get_recommendations(track_uri)

    # Print recommended songs
    print(f"\nRecommended songs based on '{song_name}':")
    for i, track in enumerate(recommendations, start=1):
        print(f"{i}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
else:
    # Print a message if no track URI was obtained
    print("Exiting.")
