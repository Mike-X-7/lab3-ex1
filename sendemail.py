import smtplib
import getpass

# fromaddr = '<email>'
# toaddr = '<email>'
message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""

# Credentials (needed)
# username = '<youremailaddress>' Gmail
# #password = '{youremailapppassword}' 

# Username and password removed for privacy purposes.


username = raw_input("Enter Username (your gmail address) to login: ")
print "Enter your email app Password"
password =  getpass.getpass()

# fromname = 'Your-Gmail'
# toname = 'Me-Yahoo'
fromname = "Michael Green"
fromaddr = username
toname = "Michael Green"
toaddr = "likemike11@yahoo.com"
subject = "lab3-ex1"
msg = "lab3-ex1 completed, move on to the next exercise"

messagetosend = message.format(
 fromname,
 fromaddr,
 toname,
 toaddr,
 subject,
 msg)


# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()