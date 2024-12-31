from mastodon import Mastodon
from atproto import Client
import os

def hello_world():
    # set up credentials for bsky
    bsky_user = os.environ["BSKY_USER"]
    bsky_pass = os.environ["BSKY_PASS"]

    client = Client()
    client.login(bsky_user, bsky_pass)
    client.send_post(text="If you're reading this, it means I just successfully used the Bluesky API on my very first try.")

if __name__ == "__main__":
    hello_world()
