#!/usr/bin/env python3
"""
Join a Lichess team.

Env-vars expected
-----------------
TOR          – your personal Lichess OAuth token (with *team:write* scope)
TEAM_ID      – the team slug
CODE         – (optional) team join code if required
"""

import os
import sys
import requests

TOKEN = os.getenv("TOR")
TEAM_ID = os.getenv("TEAM_ID")
CODE = os.getenv("CODE")  # optional

if not TOKEN:
    sys.exit("❌  No TOR token provided in environment variable TOR.")
if not TEAM_ID:
    sys.exit("❌  No TEAM_ID provided in environment variable TEAM_ID.")

URL = f"https://lichess.org/api/team/{TEAM_ID}/join"

data = {}
if CODE:
    data["code"] = CODE

resp = requests.post(
    URL,
    headers={"Authorization": f"Bearer {TOKEN}"},
    data=data if data else None,
    timeout=15,
)

print("HTTP", resp.status_code)
print(resp.text)

if resp.status_code != 200:
    sys.exit("❌  join failed")
