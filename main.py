import smtplib
import datetime
import time
import random
import pandas
import fileinput

my_email = "mustafakhan98@gmail.com"
password = "PASSWORD"

dt = datetime.datetime.now()

year = dt.year
month = dt.month
day = dt.day


data = pandas.read_csv("birthdays.csv")

count = 0
x = True
heavy = (data.loc[data["month"] == month])
# heavy5 = heavy5.tolist()
# print(heavy)
heavy3 = (data.loc[data["month"] == month])  # prints month 2
# print(heavy3)
#BIRTHDAY

while x:

    heavy5 = data.loc[count].tolist()  #Turns each df to list
    count += 1
    # print(heavy5)
    if heavy5[3] == month and heavy5[4] == day:

        f = open("letter_3.txt", 'r')
        filedata = f.read()
        f.close()

        name = (heavy5[0])
        newdata = filedata.replace("[NAME]", name)
        f = open("letter_3.txt", 'w')
        f.write(newdata)
        f.close()

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Happy Birthday\n\n{newdata}"
                            )
        connection.close()

        f = open("letter_3.txt", 'r')
        filedata = f.read()
        f.close()

        newdata = filedata.replace(name, "[NAME]")
        f = open("letter_3.txt", 'w')
        f.write(newdata)
        f.close()

        x = False

#MOTIVATIONAL QUOTE

day_of_week = dt.weekday()

if day_of_week == 0:
    with open("quotes.txt") as quotes:
        quote = quotes.readlines()
        ran_quote = random.choice(quote)

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Monday Motivation\n\n{ran_quote}!"
                            )












