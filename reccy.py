# reccy.py by Tanmay Gupta
# This program uses the Spotify API to generate song recommendations based on a given song.
# Features a visual component with background processes.

# Import necessary modules from Spotipy library:
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
# Modules for the UI:
from tkinter import *
from tkinter import ttk


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

# Function to get track recommendations based on a track name:
def get_recommendations_by_name(song_name):
    track_uri = get_track_uri(song_name)
    if track_uri:
        recommendations = get_recommendations(track_uri)
        return recommendations
    else:
        return None


######################
root = Tk()
root.title("Reccy")

# Function for creating empty lines:
def emptyline(root):
    empty_space = ttk.Label(root, text='')
    empty_space.pack()

# Top label
app_label = ttk.Label(root, text="Get Reccy'd Now", justify="center")
app_label.pack()

# Entering song name, with free-text field:
name_question = ttk.Label(root, text='Enter your song name:')
name_question.pack(anchor="w")
# ENTRY WIDGET:
song_name = StringVar()  # 'name' string.
entry = ttk.Entry(root, width=30, textvariable=song_name)  # field is 30 characters wide.
entry.pack(anchor="w")


# Function that will insert the received user inputted song and outputted recommendations into pop-up label:
def update_reccy_label():
    selected_song = song_name.get()
    
    # Create a label to display connection messages
    connection_label = ttk.Label(root, text="")
    connection_label.pack(anchor="w")
    
    # Create a label to display recommendations
    reccy_label = ttk.Label(root, text="")
    reccy_label.pack(anchor="w")

    if not selected_song:
        # If the search bar is empty, display an error message
        connection_message = f"\nPlease enter a song name!"
        connection_label.config(text=connection_message)
    else:
        recommendations = get_recommendations_by_name(selected_song)
        if recommendations:
            # Display the connection message
            connection_message = f"\nRecommended songs based on '{selected_song}':"
            connection_label.config(text=connection_message)

            for i, track in enumerate(recommendations, start=1):
                reccy_message = f"{i}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}"
                
                # Update the text of the label with the song recommendation
                reccy_label.config(text=reccy_label.cget("text") + "\n" + reccy_message)
            emptyline(root)
        else:
            # Print a message if no track URI was obtained
            connection_message = f"\nSong not found!"
            connection_label.config(text=connection_message)

# Button for triggering the recommendation functionality:
search_button = ttk.Button(root, text="Get Recommendations", command=update_reccy_label)
search_button.pack(anchor="w")


# Main loop to run the application
root.mainloop()

'''
Sample Input:
________________________________________________________
Enter your song name:
Time to Pretend MGMT
Get Recommendations

Recommended songs based on 'Time To Pretend MGMT':

1. Second Chance by Peter Bjorn and John
2. Pork And Beans by Weezer
3. My Number by Foals
4. Electric Feel - Justice Remix by MGMT
5. Is This It by The Strokes
________________________________________________________
'''
