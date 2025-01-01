from mastodon import Mastodon
from atproto import Client
import os
import html

def hello_world():
    mastodon = Mastodon(
        access_token=os.environ["MASTO_TOKEN"],
        api_base_url=os.environ["MASTO_URL"]
    )

    my_account = mastodon.me()
    account_id = my_account["id"]

    recents = mastodon.account_statuses(
        account_id,
        limit = 20,
        exclude_replies=True,
        exclude_reblogs=True
    )

    for post in recents:
        post["plain"] = html.unescape(post["content"])
        post["plain"] = post["plain"].replace("</p><p>", "\n\n")
        post["plain"] = post["plain"].replace("<p>", "")
        post["plain"] = post["plain"].replace("</p>", "")

    return recents

def login_bsky():
    # set up credentials for bsky
    bsky_user = os.environ["BSKY_USER"]
    bsky_pass = os.environ["BSKY_PASS"]

    client = Client()
    client.login(bsky_user, bsky_pass)

def send_to_bsky(bsky_client, post_text):
    bsky_client.send_post(text=post_text)

if __name__ == "__main__":
    hello_world()
