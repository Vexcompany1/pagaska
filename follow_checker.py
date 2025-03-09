from instabot import Bot
import time
import os

def check_follow_status(account):
    bot = Bot()
    session_path = f"sessions/{account['username']}"
    
    if os.path.exists(session_path):
        bot.load_session(account['username'])
    else:
        bot.login(username=account['username'], password=account['password'])

    followers = bot.get_user_followers(account['username'])
    return followers

def main():
    for account in INSTAGRAM_ACCOUNTS:
        followers = check_follow_status(account)
        print(f"Akun {account['username']} memiliki {len(followers)} followers")

if __name__ == "__main__":
    main()
    