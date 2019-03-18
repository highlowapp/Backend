import smtplib, ssl
class HLEmail:
  def HLEmail_send(self, sender, receiver, password, message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = sender
    receiver_email = receiver
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)
