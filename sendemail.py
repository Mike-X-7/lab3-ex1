import smtplib


# fromaddr = '<email>'
# toaddr = '<email>'
message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""

username = 'likemike303@gmail.com'
password = 'vzzvvvuwcilmfzzb'

# fromname = 'Me-Gmail'
# toname = 'Me-Yahoo'
fromname = "Michael Green"
fromaddr = username
toname = "Michael Green"
toaddr = "likemike11@yahoo.com"
# subject = 'Hello world.'
# msg = 'this is a test'
subject = "lab3-ex1"
msg = "Once you have it working add the script to your github account as a new repository."

messagetosend = message.format(
 fromname,
 fromaddr,
 toname,
 toaddr,
 subject,
 msg)

# Credentials (if needed)
# username = '<email>'
# #password = '{youremailapppassword}'' vzzvvvuwcilmfzzb

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()