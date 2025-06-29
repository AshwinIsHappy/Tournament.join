#!/usr/bin/env python3
"""
Join a Lichess team.

Env-vars expected
-----------------
TOR          – your personal Lichess OAuth token (with *team:write* scope)
TEAM_ID      – the team slug
"""

import os
import sys
import requests

TOKEN = os.getenv("TOR")
TEAM_ID = os.getenv("TEAM_ID")

if not TOKEN:
    sys.exit("❌  No TOR token provided in environment variable TOR.")
if not TEAM_ID:
    sys.exit("❌  No TEAM_ID provided in environment variable TEAM_ID.")

URL = f"https://lichess.org/api/team/{TEAM_ID}/join"

resp = requests.post(
    URL,
    headers={"Authorization": f"Bearer {TOKEN}"},
    timeout=15,
)

print("HTTP", resp.status_code)
print(resp.text)

if resp.status_code != 200:
    sys.exit("❌  join failed")
