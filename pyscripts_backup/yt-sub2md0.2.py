
# youtube subtitles to md

import tkinter as tk
from tkinter import simpledialog
import yt_dlp as youtube_dl

def download_subtitles(video_url):
    ydl_opts = {
        'writesubtitles': True,   # Write subtitle file
        'subtitleslangs': ['en'], # Preferred subtitle language
        'skip_download': True,    # Skip downloading the video
        'outtmpl': 'subtitles.srt', # Output filename template
        'quiet': False,
        'verbose': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def get_url():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    video_url = simpledialog.askstring("Input", "Enter the YouTube video URL:")
    if video_url:
        download_subtitles(video_url)
    root.mainloop()

# Run the function to get URL input
get_url()
