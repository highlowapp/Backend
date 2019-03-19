from HLEmail import HLEmail
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import html2text

class Convert_to_html:
  #The function that adds html to the message
  def add_html_plaintext(self, sender, receiver, password, message):
    send = HLEmail()
    #Fetch the message
    html_message = ""
    with open(message, "r") as file:
      html_message = file.read()
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

    send.HLEmail_send( sender=sender, receiver=receiver, password=password, message=mime_message )