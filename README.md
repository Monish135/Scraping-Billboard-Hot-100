# Billboard Hot 100 Scraper

A Python application that scrapes the Billboard Hot 100 chart for a specific date and creates a Spotify playlist with the top songs.

## Features

- Scrapes Billboard Hot 100 chart for any date
- Displays the top 100 songs with their artists
- Creates a private Spotify playlist with the songs
- Handles errors gracefully
- User-friendly interface

## Prerequisites

- Python 3.7 or higher
- Spotify Developer Account
- Spotify Premium account (for playlist creation)

## Setup

1. Clone this repository:
```bash
git clone https://github.com/monish135/Billboard-Hot-100-Scraper.git
cd Billboard-Hot-100-Scraper
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project directory with your Spotify credentials:
```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```

4. Register your application on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new application
   - Get your Client ID and Client Secret
   - Add `http://localhost:8888/callback` to your Redirect URIs

## Usage

1. Run the script:
```bash
python main.py
```

2. Enter a date in YYYY-MM-DD format when prompted
3. View the list of top 100 songs
4. Choose whether to create a Spotify playlist with these songs

## Example

```
Which year do you want to travel to? Type the date in this format YYYY-MM-DD: 2000-01-01

Top 100 Songs:
1. Smooth - Santana feat. Rob Thomas
2. Maria Maria - Santana
3. I Knew I Loved You - Savage Garden
...

Would you like to create a Spotify playlist with these songs? (yes/no): yes
Successfully created playlist: Billboard Hot 100 - 2000-01-01
Added 95 songs to the playlist
```

## Notes

- The script will open your default web browser for Spotify authentication
- Some older songs might not be available on Spotify
- The playlist will be created as private in your Spotify account

## License

This project is licensed under the MIT License - see the LICENSE file for details. 