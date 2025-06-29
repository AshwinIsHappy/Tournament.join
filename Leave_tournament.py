#!/usr/bin/env python3
"""
Leave a Lichess arena (team-battle) tournament.

Env-vars expected
-----------------
TOR          – your personal Lichess OAuth token (with *tournament:write* scope)
TMT_ID       – the 8-character tournament ID, e.g. "doF1DMaz"
"""

import os
import sys
import requests

TOKEN = os.getenv("TOR")
TMT_ID = os.getenv("TMT_ID")

if not TOKEN:
    sys.exit("❌  No TOR token provided in environment variable TOR.")
if not TMT_ID:
    sys.exit("❌  No TMT_ID provided in environment variable TMT_ID.")

URL = f"https://lichess.org/api/tournament/{TMT_ID}/withdraw"

resp = requests.post(
    URL,
    headers={"Authorization": f"Bearer {TOKEN}"},
    timeout=15,
)

print("HTTP", resp.status_code)
print(resp.text)

if resp.status_code != 200:
    sys.exit("❌  leave failed")
