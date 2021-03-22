#######################################################################################
# SIMPLE FUNCTION TO SEND AN EMAIL VIA GMAIL
#######################################################################################
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

SENDER_EMAIL = ""
RECEIVER_EMAIL = ""
PASSWORD = ""

def send_email():

    try:
        # prepare the object responsible for sending the email
        smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(SENDER_EMAIL, PASSWORD)

        # add the subject and the email adresses
        msg = MIMEMultipart()
        msg["Subject"] = "INSERT EMAIL SUBJECT"
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL

        # add the text body (and, if needed, image attachments)
        msgText = MIMEText("INSERT EMAIL BODY", "html")
        msg.attach(msgText)

        # attach a file
        '''with open("file_name", "rb") as file:
            img = MIMEImage(file.read())
            img.add_header("Content-Disposition", "attachment", filename = "file_name")
            msg.attach(img)'''

        try:
            # send the email
            smtpObj.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

        except Exception as e:
            print(e)

        print("Email sent!")

    except Exception as e:
        print(e)
    
if(__name__ == "__main__"):

    send_email()