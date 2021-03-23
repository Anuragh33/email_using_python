import smtplib

from email.message import EmailMessage

from string import Template

from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()

email["from"] = "name"
email["to"] = "receiver mail"
email["subject"] = "You won 1000000 lakh rupees!"

email.set_content(html.substitute({"name":"harish"}),"html")

with smtplib.SMTP(host = "smtp.gmail.com", port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login("sender mail", "sender password")
	smtp.send_message(email)
	print("mail sent sucessfuly!")

