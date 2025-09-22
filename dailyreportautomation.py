import schedule
import time
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

# Step 1: Generate a sample daily report
def generate_report():
    data = {
        "User": ["Alice", "Bob", "Charlie"],
        "Access Zone": ["Zone A", "Zone B", "Zone A"],
        "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")] * 3
    }
    df = pd.DataFrame(data)
    filename = "daily_report.csv"
    df.to_csv(filename, index=False)
    return filename

# Step 2: Send report via email
def send_email(report_file):
    sender_email = "your_email@example.com"
    receiver_email = "recipient@example.com"
    password = "your_password"  # use app password for Gmail/Outlook
    
    subject = "Daily Privacy Zone Report"
    body = "Please find attached the daily privacy zone enforcement report."

    # Email setup
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    # Attach report file
    with open(report_file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {report_file}")
        msg.attach(part)

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

    print("✅ Report sent successfully!")

# Step 3: Combine everything into one task
def job():
    report = generate_report()
    send_email(report)

# Step 4: Schedule daily at 6 PM
schedule.every().day.at("18:00").do(job)

print("📅 Scheduler started. Waiting for next run...")
while True:
    schedule.run_pending()
    time.sleep(60)
