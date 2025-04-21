import requests
from bs4 import _soup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

input("Which year do you want tot travel to? Type the date in this format YYYY-MM-DD:")

URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_ID = "aa8d288d6ca649ada6a4b67dc94c011d"
SPOTIFY_SECRET = "a911b851d3f44b04b2861a84597c6c9e"

auth_manager = SpotifyClientCredentials(
    client_id = SPOTIFY_ID,
    client_secret= SPOTIFY_SECRET
)
sp = spotipy.Spotify(auth_manager = auth_manager)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(URL)
website = response.text

soup = _soup(website, "html.parser")
titles = soup.select("h3.c-title.a-no-trucate.a-font-primary-bold-s")


# title_list = [title.replace('\t','').replace("\n","") for title in title_list]
for i , title in enumerate(titles,1):
    print(f"{i}. {title.getText().strip()}")

