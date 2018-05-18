from config import client_id, client_secret
import praw
import smtplib
from email.mime.text import MIMEText
import time


def send_text(title, price, url):
    from config import sender, password
    # Define to/from
    casey = '8018217046@vtext.com'
    jarrod = '3854777637@msg.fi.google.com'

    # Create message
    msg = MIMEText("{}: {} - {}".format(title, price, url))
    msg['From'] = sender
    msg['To'] = 'KSL shoppers'

    # Create server object with SSL option
    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

    # Perform operations via server
    server.login(sender, password)
    server.sendmail(sender, [casey, jarrod], msg.as_string())
    server.quit()


# Reddit part
mapping = {
    "1080 ti": 700.0,
    "1080ti": 700.0
}

def process_title(title):
    stitle = title.replace('[','').split(']')
    if 'USA' not in stitle[0]:
        return False, False
    have = stitle[2][:-1]
    want = stitle[3]
    return have, want

u_agent = 'web:hardwarehelper:v0.0.1 (by /u/mauza11)'
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=u_agent)

for submission in reddit.subreddit('hardwareswap').new(limit=10):
    min_old = (time.time()-submission.created_utc)/60
    if min_old > 10:
        continue
    have, want = process_title(submission.title)
    if have:
        for item, cost in mapping.items():
            if item in have:
                send_text(submission.title, '?', submission.url)
