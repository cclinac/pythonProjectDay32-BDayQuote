import smtplib
my_email = "linji3100429@gmail.com"
to_email = "jimjimlin@gmail.com"
password = "epoadynjpbgaicqs"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_email,
        msg="Subject:Hello\n\nHi! This the body of my mail.")

