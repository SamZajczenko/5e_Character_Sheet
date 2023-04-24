import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def email():
    # Attachment for organization.
    email = input("What email would you like your character sheet to be sent to? ")
    message = ("Here is your character sheet. ")
    msg=MIMEMultipart()
    msg['From'] = "samzajc@gmail.com"
    msg['To'] = email
    msg['Subject'] = "Character sheet created."
    msg.attach(MIMEText(message, 'plain'))
    filename="new_charactersheet.pdf"
    attachment=open(filename, 'rb')
    part=MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("samzajc@gmail.com", "")
    text = msg.as_string()
    server.sendmail(msg['From'], msg['To'], text)
    server.quit()