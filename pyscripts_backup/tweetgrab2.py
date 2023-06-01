import os
import tweepy
import requests
from datetime import datetime, timedelta

# Twitter API credentials
consumer_key = 'aBgejrp6NtjxGtRYmV5sayCLX'
consumer_secret = 'g8oaHiLBovzmHtkD4TtxPw2W8jPqRBVdiOTJwmKohyUY4PA6SV'
access_token = '1330798174253019137-pbr2Exd7aulXy93WwH3jGhT0QyKGaq'
access_token_secret = 'yqptnpY8NCKNh1UhobXSCtaeJjU1Yks1mLGcppGNguISZ'

def download_liked_images(output_dir):
    # Authenticate with the Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Calculate the date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=60)

    # Get the liked tweets
    liked_tweets = api.get_favorites(count=200)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Download the images from the liked tweets
    for tweet in liked_tweets:
        if start_date <= tweet.created_at <= end_date:
            media_entities = tweet.entities.get('media', [])
            for media_entity in media_entities:
                media_url = media_entity['media_url']
                filename = os.path.basename(media_url)
                image_path = os.path.join(output_dir, filename)
                response = requests.get(media_url, stream=True)
                if response.status_code == 200:
                    with open(image_path, 'wb') as f:
                        for chunk in response.iter_content(1024):
                            f.write(chunk)
                    print(f"Downloaded: {image_path}")

    print("Download completed!")

# Replace 'YOUR_OUTPUT_DIRECTORY' with the desired directory path where you want to save the downloaded pictures
download_liked_images('H:\VLADMATIK\Bang_intertext_research\Style_Aesthetic\tweetgrab')
