from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

request = youtube.search().list(
    q="wooting keyboard",
    part="snippet",
    type="video",
    maxResults=5
)

response = request.execute()

for item in response["items"]:
    print("=" * 50)
    print("Title:", item["snippet"]["title"])
    print("Channel:", item["snippet"]["channelTitle"])
    print("Published:", item["snippet"]["publishedAt"])
    print("Video ID:", item["id"]["videoId"])