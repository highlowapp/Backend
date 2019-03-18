from HLEmail import HLEmail
sender = input("What is your admin email? ")
password = input("What is your admin password? ")
receiver = input("What is the email of the person receiving this? ")
with open("testMessage.txt", "r") as file:
  message = file.read()
send = HLEmail()
#This is the order in which you enter the values: sender, receiver, password, message
send.HLEmail_send( sender=sender, receiver=receiver, password=password, message=message )

