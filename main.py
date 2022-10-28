import smtplib, ssl
smtp_server = "smtp.gmail.com"
port = 587
sender_email = "harsith.rajkumar@gmail.com"
receiver_email = "sanjeevrh07@gmail.com"
password = "accaibbgzvaywpil"
message = ""
context = ssl.create_default_context()
try:
    server = smtplib.SMTP(smtp_server,port)
    server.starttls(context=context)
    server.login(sender_email,password)
    server.sendmail(sender_email, receiver_email, message)
finally:
    server.quit()