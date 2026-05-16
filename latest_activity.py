import os
from dotenv import load_dotenv
from stravalib.client import Client

load_dotenv()

ACCESS_TOKEN = os.getenv("STRAVA_ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise Exception("Missing STRAVA_ACCESS_TOKEN in .env")

# Create Strava client
client = Client(access_token=ACCESS_TOKEN)

# Get most recent activity
activities = client.get_activities(limit=1)

latest = next(activities)

print("\n🏃 Most Recent Activity\n")

print(latest)