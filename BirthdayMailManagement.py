import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from BirthdateWish import BirthdateWish

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def send_mail(config, birth_date_wish: BirthdateWish):
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(config["mail-mail"], config["mail-password"])

    msg = MIMEMultipart()
    message = read_template(config["template-file"]).substitute(PERSON_NAME=birth_date_wish.name, OWN_NAME=config['sender'])

    msg['From'] = 'pythontest122@gmail.com'
    msg['To'] = birth_date_wish.email
    msg['Subject'] = config["subject-line"]
    msg.attach(MIMEText(message, 'plain'))

    s.send_message(msg)
