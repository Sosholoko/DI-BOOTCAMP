from . import mail_manager
import flask_mail

def send_mail(title, body, recipients, html=""):
    
    if type(recipients) == str:
        recipients = [recipients]
    
    msg = flask_mail.Message(
        subject = title,
        body = body,
        html=html,
        recipients = recipients,
    )

    mail_manager.send(msg)




