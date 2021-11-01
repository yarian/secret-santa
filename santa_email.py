import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from secrets import SENDER_EMAIL, SENDER_NAME, GMAIL_APP_PWD

from contextlib import contextmanager

@contextmanager
def email_session():
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(SENDER_EMAIL, GMAIL_APP_PWD)
    try:
        yield session
    finally:
        session.quit()

def send_email(email_session, to_addr, mail_content):
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = to_addr
    message['Subject'] = 'Your Secret Santa Mission'
    message.attach(MIMEText(mail_content, 'html'))
    text = message.as_string()
    email_session.sendmail(SENDER_EMAIL, to_addr, text)
    print(f'Message {message} sent to {to_addr}')
    print("=" * 50)

def send_secret_santa_email(email_session, gifter, recipient):
    if recipient.gift_preferences:
        sanitized_preferences = recipient.gift_preferences.replace("\n", "<br>")
        preferences = f"""
{recipient.name} wroted the following as their gift preferences:
<blockquote>
{sanitized_preferences}
</blockquote>
"""
    else:
        preferences = f"""
{recipient.name} did not write anything for their gift preferences. Good luck! 😂
"""

    mail_content = f"""
<html>
  <head></head>
  <body>
    <p>Hi {gifter.name},</p>
    <p>You are {recipient.name}'s secret santa!</p>
    <p>{preferences}</p>
    <p>Remember the spend limit is $some_amount.</p>
    <p>Cheers,</p>
    <p>-{SENDER_NAME}<p>
  </body>
</html>
"""
    send_email(email_session, gifter.email, mail_content)