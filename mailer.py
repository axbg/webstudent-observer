import smtplib
import validators
import credentials
import requests

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mailgun(mail_body):
    validators.validate_mailgun_credentials()

    request_url = 'https://api.mailgun.net/v3/{0}/messages'.format(
        credentials.MAILGUN_SANDBOX)
    request = requests.post(request_url, auth=('api', credentials.MAILGUN_KEY), data={
        'from': credentials.MAIL_FROM,
        'to': credentials.MAIL_TO,
        'subject': credentials.MAIL_SUBJECT,
        'text': mail_body
    })


def send_mail_smtp(mail_body):
    validators.validate_smtp_credentials()

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(credentials.GMAIL_USER, credentials.GMAIL_DEVICE_KEY)

    msg = MIMEMultipart('alternative')
    msg['FROM'] = credentials.MAIL_FROM
    msg['To'] = credentials.MAIL_TO
    msg['Subject'] = credentials.MAIL_SUBJECT
    msg.attach(MIMEText(mail_body.encode('utf-8'), _charset='utf-8'))

    server.sendmail(credentials.GMAIL_USER,
                    credentials.MAIL_TO, msg.as_string())
    server.close()


def send_mail(mail_body):
    if credentials.MAIL_SERVICE == "MAILGUN":
        send_mailgun(mail_body)
    else:
        send_mail_smtp(mail_body)
