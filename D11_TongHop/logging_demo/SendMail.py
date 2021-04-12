import smtplib, ssl
import logging
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def setup_log():
    logging.getLogger("NHATNGHE")

    # Setup level xuất hiện log
    logging.basicConfig(
        level=logging.INFO,
        filename='maillog_{:%Y_%m_%d}.log'.format(datetime.now()),
        filemode="a", # a: append, w: write
        format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s :line %(lineno)s : %(message)s'
    )

gmail_user = 'pynhatnghe@gmail.com'
gmail_password = 'input_pass'

def send_mail(receive_list, content):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, receive_list, content)
        server.close()
    except Exception as e:
        logging.error(e)


def send_mail_with_format(receive_list, subject, content):
    try:
        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (gmail_user, ", ".join(receive_list), subject, content)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, receive_list, email_text)
        server.close()
    except Exception as e:
        logging.error(e)


def send_mail_with_html_format(receive_list, subject, content):
    try:
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = gmail_user
        message["To"] = receive_list

        # Set format email plain/html MIMEText objects
        part = MIMEText(content, "html")
        message.attach(part)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(gmail_user, gmail_password)
            server.sendmail(
                gmail_user, receive_list, message.as_string()
            )
    except Exception as e:
        logging.error(e)

setup_log()
# send_mail(["aspnhatnghe@gmail.com"], "Test mail")

# send_mail_with_format([
#     "aspnhatnghe@gmail.com", "pynhatnghe@gmail.com"],
#                       "Send mail", "Test mail")


html_email_content = """\
<!DOCTYPE html>
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://nhatnghe.com" style="color:red">Python Nhat Nghe</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""
send_mail_with_html_format(
    # ",".join(["aspnhatnghe@gmail.com", "pynhatnghe@gmail.com"]),
    "aspnhatnghe@gmail.com,pynhatnghe@gmail.com",
    "Send mail wih HTML format", html_email_content)
