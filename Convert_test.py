from Convert import Convert_to_html

sender = input("What is your admin email? ")
password = input("What is your admin password? ")
receiver = input("What is the email of the person receiving this? ")
message = "testEmail.html"

convert = Convert_to_html()

convert.add_html_plaintext( sender=sender, receiver=receiver, password=password, message=message )