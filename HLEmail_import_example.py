from HLEmail import HLEmail
sender = input("What is your admin email? ")
password = input("What is your admin password? ")
receiver = input("What is the email of the person receiving this? ")
#admin = HLEmail(sender=sender, password=password)
with open("testEmail.html", "r") as file:
  message = file.read()
send = HLEmail(sender, password)
#This is the order in which you enter the values: receiver, message
send.send_html_email( receiver=receiver, message=message )
