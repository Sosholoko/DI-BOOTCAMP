from . import mail_manager
import flask_mail



def send_mail(title, body, recipients, html=""):

    if type(recipients) == str:
        recipients = [recipients]

    # Create a message object
    msg = flask_mail.Message(
        subject=title,
        body=body,
        html=html,
        recipients=recipients,
    )

    # Send it using mail_manager.send
    mail_manager.send(msg)

