# 🚴 strava-data-for-readme

Live Strava data for your GitHub profile README

---

## ⚡ Step 1 — Setup `.env`

Create a `.env` file in the project root:

```env
STRAVA_CLIENT_ID=YOUR_CLIENT_ID
STRAVA_CLIENT_SECRET=8498f6c58c78208abfc8e25d44abcbbdb10ee327
```

Run the setup script:
./venv/bin/python token_setup.py

## 🌐 Step 3 — Follow login flow

- A browser window will open
- Log in to Strava
- Approve permissions
- Copy the authorization code

```
http://localhost/?state=&code={YOUR CODE WILL BE HERE}d&scope=read,activity:read_all,profile:read_all
```

This will generate:

- `STRAVA_ACCESS_TOKEN`
- `STRAVA_REFRESH_TOKEN`
