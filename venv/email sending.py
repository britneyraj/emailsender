import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html= Template(Path("C:\email sender\emailfile.html").read_text())
email=EmailMessage()
email['from']='loverofcake1999@outlook.com'
email['to']='dmjbritney@gmail.com'
email['subject']='You won 1000 dollars'

email.set_content(html.substitute({'name': 'Britney'}), 'html')


with smtplib.SMTP(host='smtp.office365.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('loverofcake1999@outlook.com', 'nilaismydogsname!')
    smtp.send_message(email)
    print('all good')
