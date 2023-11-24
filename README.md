# Reccy-MusicRecommender
Reccy - The personalized music recommender! Accesses Spotify's API using Flask and the "Spotipy" libraries to generate music recommendations for your specified songs!

Files:
* beta.py: Working text-based prototype of Reccy. Uses the terminal for prompts and responses.
* reccy.py: Final release of Reccy with a pop-up UI display.
* server.py: Background checking for Spotify API access through local server.

How it works:
* Running reccy.py opens a pop-up window which prompts the user to enter a song name.
* After entering a song name, the program matches your song name to what it thinks you mean, finds song matches based on the genre(s), audience, and artist.
* Program prints 5 song recommendations and is ready to be used again for another prompt.
