import youtube_dl

def download_video(url, output_path):
    try:
        ydl_opts = {
            'outtmpl': output_path + '/%(title)s.%(ext)s',
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', 'video')
            print("Downloading:", video_title)
            ydl.download([url])
            print("Download complete!")

    except Exception as e:
        print("An error occurred:", str(e))

# Prompt the user for the YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Prompt the user for the output path to save the video
output_path = input("Enter the output path to save the video: ")

# Call the download_video function with the provided URL and output path
download_video(video_url, output_path)
