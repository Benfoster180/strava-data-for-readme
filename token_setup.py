import webbrowser
import os
from dotenv import load_dotenv
from stravalib.client import Client

load_dotenv()

STRAVA_CLIENT_ID = int(os.getenv("STRAVA_CLIENT_ID"))
STRAVA_CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")

client = Client()

# Permissions you want
request_scope = [
    "read",
    "activity:read_all",
    "profile:read_all"
]

# MUST match your Strava API settings
redirect_url = "http://localhost"

# Generate authorization URL
url = client.authorization_url(
    client_id=STRAVA_CLIENT_ID,
    redirect_uri=redirect_url,
    scope=request_scope,
)

print("\nOpening browser for Strava authorization...\n")

webbrowser.open(url)

print("""
After approving access, your browser will redirect to something like:

http://localhost/?state=&code=abc123xyz&scope=read,activity:read_all

Copy ONLY the code value.
""")

# Paste the code from browser URL
code = input("Paste code here: ")

# Exchange code for tokens
token_response = client.exchange_code_for_token(
    client_id=STRAVA_CLIENT_ID,
    client_secret=STRAVA_CLIENT_SECRET,
    code=code
)

# Extract tokens
access_token = token_response["access_token"]
refresh_token = token_response["refresh_token"]

# Save directly into .env
with open(".env", "a") as f:
    f.write(f"\nSTRAVA_ACCESS_TOKEN={access_token}")
    f.write(f"\nSTRAVA_REFRESH_TOKEN={refresh_token}\n")

print("\n✅ Tokens saved to .env successfully!")
print("You should only need to do this once.")