from gift_pairing import GiftPairings
from santa_email import email_session, send_secret_santa_email
from people import PEOPLE

pairing = GiftPairings(PEOPLE)
for gifter, recipient in pairing:
    with email_session() as session:
        send_secret_santa_email(session, gifter, recipient)
