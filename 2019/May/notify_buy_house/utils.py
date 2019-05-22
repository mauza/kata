import smtplib
from email.mime.text import MIMEText

from config import SMTP_USER, SMTP_PASSWORD

def send_text(url, sent_to_list):
    # Create message
    msg = MIMEText("{}".format(url))
    msg['From'] = SMTP_USER
    msg['To'] = 'House shoppers'

    # Create server object with SSL option
    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

    # Perform operations via server
    server.login(SMTP_USER, SMTP_PASSWORD)
    server.sendmail(SMTP_USER, sent_to_list, msg.as_string())
    server.quit()
