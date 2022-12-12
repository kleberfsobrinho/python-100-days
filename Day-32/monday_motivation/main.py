import smtplib
from secret_data import my_email, password
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as data:
        lines = data.readlines()
        quote = random.choice(lines)

    # send email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # security
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{quote}."
        )
