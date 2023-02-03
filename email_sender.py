from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib, ssl
import pandas
import os

host = "smtp.gmail.com"
port = 465

username = "donotreplybackiwillnotrespond@gmail.com"
password = os.getenv("PASSWORD")
#def reciever(recieving_email):
  #reciever = recieving_email
  #return reciever


context = ssl.create_default_context()


def send_email(file, reciever):
  my_file = pandas.read_csv(file)
  message = MIMEMultipart()
  message["Subject"] = "Chess Tournament Data"
  message["From"] = "donotreplybackiwillnotrespond@gmail.com"

  text = """\
  <html>
    <head></head>
    <body>
      {0}
    </body>
  </html>
  """.format(my_file.to_html())

  part1 = MIMEText(text, "html")

  message.attach(part1)

  """"server = smtplib.SMTP(host=host, port=port)
  server.login(username, password)
  server.sendmail(from_addr = message['From'], to_addrs = reciever , msg = message.as_string())
  server.quit()"""
  with smtplib.SMTP_SSL(host, port, context=context) as server:
      server.login(username, password)
      server.sendmail(from_addr = message['From'], to_addrs = reciever , msg = message.as_string())
      server.quit()