import csv
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# =========================
# EMAIL CONFIGURATION
# =========================

SENDER_EMAIL = "rohanhair78@gmail.com"
APP_PASSWORD = "rteuzfoqkiiukhrv"

SUBJECT = "Internship Update"

MESSAGE = """
Hello {name},

I hope you are doing well.

This is an automated email from my Python Email Automation System.

Thank you.

Regards,
Rohan
"""


# =========================
# SEND EMAIL FUNCTION
# =========================

def send_email(receiver_email, receiver_name):
    try:
        message = MIMEMultipart()
        message["From"] = SENDER_EMAIL
        message["To"] = receiver_email
        message["Subject"] = SUBJECT

        personalized_message = MESSAGE.format(name=receiver_name)

        message.attach(MIMEText(personalized_message, "plain"))

        server.sendmail(
            SENDER_EMAIL,
            receiver_email,
            message.as_string()
        )

        print(f"✅ Email sent to {receiver_name} - {receiver_email}")
        return True

    except Exception as e:
        print(f"❌ Failed for {receiver_email}: {e}")
        return False


# =========================
# MAIN PROGRAM
# =========================

print("\n==============================")
print("   PYTHON EMAIL AUTOMATION")
print("==============================\n")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SENDER_EMAIL, APP_PASSWORD)

success = 0
failed = 0

with open("recipients.csv", "r", newline="", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        name = row["name"]
        email = row["email"]

        if send_email(email, name):
            success += 1
        else:
            failed += 1

        # 3-second delay
        time.sleep(3)

server.quit()

print("\n==============================")
print("         COMPLETED")
print("==============================")
print(f"Emails sent : {success}")
print(f"Failed      : {failed}")
print("==============================")
