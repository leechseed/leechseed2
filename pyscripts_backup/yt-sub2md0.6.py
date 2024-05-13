import tkinter as tk
from tkinter import simpledialog
import yt_dlp as youtube_dl
import re

def clean_filename(text):
    """Sanitize filenames by replacing unwanted characters."""
    return re.sub(r'[\\/*?:"<>|]', '', text)

def download_subtitles(video_url):
    # Extract video info without downloading
    with youtube_dl.YoutubeDL({'quiet': False, 'verbose': True}) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
    
    title = info_dict.get('title', 'Unknown_Title')
    uploader = info_dict.get('uploader', 'Unknown_Channel')

    # Clean and format filename
    filename = f"{clean_filename(uploader)}_{clean_filename(title)}.srt"

    # Setup download options with dynamic filename
    ydl_opts = {
        'writesubtitles': True,
        'subtitleslangs': ['en'],
        'skip_download': True,
        'quiet': False,
        'verbose': True,
        'outtmpl': filename,  # Apply the dynamic filename here
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([video_url])
        if result != 'finished':  # Check if download was not successful
            print("No subtitles were downloaded.")
        else:
            print(f"Subtitles downloaded and saved as: {filename}")

def get_url():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    video_url = simpledialog.askstring("Input", "Enter the YouTube video URL:")
    if video_url:
        download_subtitles(video_url)
    root.destroy()  # Ensure the Tkinter root window is properly destroyed

# Run the function to get URL input
get_url()
