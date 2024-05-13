import tkinter as tk
from tkinter import simpledialog
import yt_dlp as youtube_dl
import re

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
    convert_srt_to_md('subtitles.srt', 'documentation.md')

def convert_srt_to_md(srt_filename, md_filename):
    try:
        with open(srt_filename, 'r', encoding='utf-8') as file:
            srt_content = file.read()

        # Use regex to parse the SRT file and extract subtitles and timestamps
        pattern = re.compile(r'\d+\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+?)(?=\n\n|\Z)', re.DOTALL)
        matches = pattern.findall(srt_content)

        md_content = ['# Video Subtitles Documentation\n\n']
        
        for start, end, text in matches:
            text = text.replace('\n', ' ')  # Replace newlines in subtitles with space
            md_content.append(f'- {text} <!-- {start} to {end} -->')

        # Write formatted Markdown content
        with open(md_filename, 'w', encoding='utf-8') as file:
            file.write('\n'.join(md_content))
    except FileNotFoundError:
        print("The SRT file was not found.")

def get_url():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    video_url = simpledialog.askstring("Input", "Enter the YouTube video URL:")
    if video_url:
        download_subtitles(video_url)
    root.mainloop()

# Run the function to get URL input
get_url()
