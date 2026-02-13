import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
from google import genai
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/send', methods=['POST'])
def send_email():

    # Get form data
    name = request.form['name']
    manager_name = request.form['manager_name']
    to_email = request.form['to_email']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    reason = request.form['reason']
    colleague_name = request.form.get('colleague_name')

    # Format dates naturally
    start_date = datetime.strptime(start_date, "%Y-%m-%d").strftime("%d %B %Y")
    end_date = datetime.strptime(end_date, "%Y-%m-%d").strftime("%d %B %Y")

    # Optional colleague sentence
    if colleague_name:
        colleague_line = f"I have informed {colleague_name} to handle my responsibilities during my absence."
    else:
        colleague_line = ""

    # Improved professional prompt
    prompt = f"""
Write a professional and slightly detailed sick leave email.

Address the manager respectfully as:
Dear Mr./Ms. {manager_name},

Employee Name: {name}
Leave Start Date: {start_date}
Leave End Date: {end_date}
Reason: {reason}

Additional Context:
{colleague_line}

Requirements:
- Greeting must be respectful (Dear Mr./Ms. {manager_name},)
- Make the body slightly detailed but concise.
- Mention health condition politely.
- Assure work continuity.
- Maintain professional tone.
- Do NOT use markdown.
- Do NOT use asterisks.
- Do NOT include explanations or placeholders.
- Return only the email body.
"""

    # Generate with Gemini 2.5 Flash
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    email_body = response.text

    # Remove any accidental markdown formatting
    email_body = email_body.replace("**", "")
    email_body = email_body.replace("*", "")

    # Send email
    msg = EmailMessage()
    msg['Subject'] = "Sick Leave Application"
    msg['From'] = os.getenv("EMAIL_ADDRESS")
    msg['To'] = to_email
    msg.set_content(email_body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD"))
        server.send_message(msg)

    return "Email Sent Successfully!"

if __name__ == "__main__":
    app.run(debug=True)
