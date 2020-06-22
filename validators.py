import credentials


def validate_login_credentials():
    assert credentials.WEBSTUDENT_ACCOUNT != "", "WEBSTUDENT_ACCOUNT variable is empty"
    assert credentials.WEBSTUDENT_PASSWORD != "", "WEBSTUDENT_PASSWORD variable is empty"


def validate_mailgun_credentials():
    validate_mail_variables()
    assert credentials.MAILGUN_KEY != "", "MAILGUN_KEY variable is empty"
    assert credentials.MAILGUN_SANDBOX != "", "MAILGUN_SANDBOX variable is empty"


def validate_smtp_credentials():
    validate_mail_variables()
    assert credentials.GMAIL_DEVICE_KEY != "", "GMAIL_DEVICE_KEY variable is empty"
    assert credentials.GMAIL_USER != "", "GMAIL_USER variable is empty"


def validate_mail_variables():
    assert credentials.MAIL_FROM != "", "MAIL_FROM variable is empty"
    assert credentials.MAIL_TO != "", "MAIL_TO variable is empty"
    assert credentials.MAIL_SUBJECT != "", "MAIL_SUBJECT variable is empty"
