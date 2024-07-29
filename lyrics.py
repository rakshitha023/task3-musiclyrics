import tkinter as tk
from tkinter import messagebox
import requests

def get_lyrics(artist, song):
    url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('lyrics', 'No lyrics found.')
    else:
        return "Lyrics not found or an error occurred."

def show_lyrics():
    artist = artist_entry.get()
    song = song_entry.get()
    if artist and song:
        lyrics = get_lyrics(artist, song)
        lyrics_text.delete(1.0, tk.END)
        lyrics_text.insert(tk.END, lyrics)
    else:
        messagebox.showwarning("Input Error", "Please enter both artist and song name.")

# Set up the main application window
root = tk.Tk()
root.title("Lyrics Extractor")

# Create and place the artist label and entry
artist_label = tk.Label(root, text="Artist:")
artist_label.pack(pady=5)
artist_entry = tk.Entry(root, width=50)
artist_entry.pack(pady=5)

# Create and place the song label and entry
song_label = tk.Label(root, text="Song:")
song_label.pack(pady=5)
song_entry = tk.Entry(root, width=50)
song_entry.pack(pady=5)

# Create and place the button to get lyrics
get_lyrics_button = tk.Button(root, text="Get Lyrics", command=show_lyrics)
get_lyrics_button.pack(pady=20)

# Create and place the text area to display lyrics
lyrics_text = tk.Text(root, height=20, width=60)
lyrics_text.pack(pady=5)

# Start the GUI event loop
root.mainloop()