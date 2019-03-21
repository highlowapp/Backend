import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, ssl
from email.mime.text import MIMEText
import html2text

class HLEmail:
  def __init__(self, sender, password):
    self.sender = sender
    self.password = password
    

  #The function that sends the email
  def HLEmail_send(self, receiver, message): 
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = self.sender
    password = self.password
    receiver_email = receiver
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message.as_string())

  #The function that adds html to the message
  def send_html_email(self, receiver, message):
    sender = self.sender
    password = self.password
    send = HLEmail(sender, password) 
    #Fetch the message
    html_message = ""
    html_message = message
    #Create a plaintext version of the HTML email
    message_plaintext = html2text.html2text( html_message )
    #Create the MIMETexts
    mime_message = MIMEMultipart("alternative")
    message_html = MIMEText( html_message, 'html' )
    message_plaintext = MIMEText( message_plaintext, 'plain')

    #Define email headers
    mime_message["Subject"] = "HTML/Plaintext email"
    mime_message["From"] = sender
    mime_message["To"] = receiver

    #Attach plaintext and HTML to message
    mime_message.attach(message_plaintext)
    mime_message.attach(message_html)

    send.HLEmail_send(  receiver=receiver,  message=mime_message )
