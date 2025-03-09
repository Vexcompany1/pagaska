from instabot import Bot
import time
import os
from config import INSTAGRAM_ACCOUNTS, TARGET_POST_URL, LIKE_LIMIT, SLEEP_TIME

def like_post(account):
    bot = Bot()
    session_path = f"sessions/{account['username']}"

    if os.path.exists(session_path):
        bot.load_session(account['username'])
    else:
        bot.login(username=account['username'], password=account['password'])

    post_id = bot.get_media_id_from_link(TARGET_POST_URL)

    for _ in range(LIKE_LIMIT):
        bot.like(post_id)
        print(f"Akun {account['username']} berhasil like {TARGET_POST_URL}")
        time.sleep(SLEEP_TIME)

def main():
    for account in INSTAGRAM_ACCOUNTS:
        like_post(account)

if __name__ == "__main__":
    main()
