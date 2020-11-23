import pandas as pd
import smtplib

e = pd.read_excel("Emails.xlsx") # In this file we will add any emails we want to send

emails = e['emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("youemail", "yourpassword")
msg = "Do you want to purchase Iphone but don't have enough money, We are presenting you an oppurtunity to win Iphone, our website provides you the most opportunity to win Iphone, the chances of getting Iphone are at your doorstep waiting for your click just click on our website Signup & win Iphone. Website is given below: https://www.iphone11pro-go.com/"
subject = "Wanna Win an IPhone!"
body = "Subject: {}\n\n{}".format(subject, msg)

for email in emails:
    server.sendmail("Your Email here", email, body)
    print("Emails Send Successfully...")
server.quit()