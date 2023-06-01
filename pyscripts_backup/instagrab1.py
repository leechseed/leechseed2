import os
from datetime import datetime

import instaloader

def download_saved_pictures(username, password, output_dir, start_date, end_date):
    # Create an instance of the Instaloader
    loader = instaloader.Instaloader()

    # Login to your Instagram account
    loader.login(username, password)

    # Get the profile of the logged-in user
    profile = instaloader.Profile.from_username(loader.context, username)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Convert start_date and end_date to datetime objects
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d')

    # Download the saved pictures within the specified time frame
    for post in profile.get_saved_posts():
        post_datetime = datetime.fromtimestamp(post.date_utc.timestamp())
        if start_datetime <= post_datetime <= end_datetime:
            loader.download_post(post, target=os.path.join(output_dir, '{date_utc:%Y-%m-%d}_saved_{shortcode}'))

    print("Download completed!")

# Replace 'YOUR_USERNAME', 'YOUR_PASSWORD', 'OUTPUT_DIRECTORY', 'START_DATE', and 'END_DATE' with your actual credentials, desired output directory path, and the time frame you want to download pictures from
download_saved_pictures('agomanrafa', '8Kef2!t2edfQjEc', 'H:\VLADMATIK\Bang_intertext_research\Style_Aesthetic\Instagrabs', '2023-03-01', '2023-05-31')
