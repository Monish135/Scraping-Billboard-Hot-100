import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_billboard_songs(date):
    """Get the top 100 songs from Billboard for a specific date."""
    URL = f"https://www.billboard.com/charts/hot-100/{date}/"
    
    try:
        response = requests.get(URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Get song titles and artists
        song_titles = [title.getText().strip() for title in soup.select("h3.c-title.a-no-trucate.a-font-primary-bold-s")]
        song_artists = [artist.getText().strip() for artist in soup.select("span.c-label.a-no-trucate.a-font-primary-s")]
        
        return list(zip(song_titles, song_artists))
    except Exception as e:
        print(f"Error fetching Billboard data: {e}")
        return []

def create_spotify_playlist(date, songs):
    """Create a Spotify playlist with the top 100 songs."""
    try:
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri="http://localhost:8888/callback",
                client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
                show_dialog=True,
                cache_path="token.txt"
            )
        )
        
        user_id = sp.current_user()["id"]
        playlist_name = f"Billboard Hot 100 - {date}"
        
        # Create playlist
        playlist = sp.user_playlist_create(
            user=user_id,
            name=playlist_name,
            public=False,
            description=f"Top 100 songs from Billboard on {date}"
        )
        
        # Search for songs and add to playlist
        song_uris = []
        for title, artist in songs:
            try:
                result = sp.search(q=f"track:{title} artist:{artist}", type="track")
                if result["tracks"]["items"]:
                    song_uris.append(result["tracks"]["items"][0]["uri"])
            except Exception as e:
                print(f"Error searching for {title} by {artist}: {e}")
        
        # Add songs to playlist
        if song_uris:
            sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
            print(f"Successfully created playlist: {playlist_name}")
            print(f"Added {len(song_uris)} songs to the playlist")
        else:
            print("No songs were found to add to the playlist")
            
    except Exception as e:
        print(f"Error creating Spotify playlist: {e}")

def main():
    while True:
        try:
            date_str = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD (or 'quit' to exit): ")
            
            if date_str.lower() == 'quit':
                break
                
            # Validate date format
            try:
                datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD")
                continue
            
            # Get songs from Billboard
            songs = get_billboard_songs(date_str)
            
            if songs:
                print("\nTop 100 Songs:")
                for i, (title, artist) in enumerate(songs, 1):
                    print(f"{i}. {title} - {artist}")
                
                # Create Spotify playlist
                create_spotify = input("\nWould you like to create a Spotify playlist with these songs? (yes/no): ")
                if create_spotify.lower() == 'yes':
                    create_spotify_playlist(date_str, songs)
            
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

