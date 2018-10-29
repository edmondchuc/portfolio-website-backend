from flask import Flask, render_template, request

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

app = Flask(__name__)

# read the email address from file
EMAIL_TO = None
with open('email_to.txt', 'r') as myfile:
    EMAIL_TO=myfile.read().replace('\n', '')
    EMAIL_TO=Email(EMAIL_TO)


@app.route('/contact', methods=['POST'])
def contact():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email_from = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    subject = f'[www.edmondchuc.com] New message from {first_name}'

    content = Content('text/plain', f"""
    New message received from www.edmondchuc.com
    
    Sender's details:    
    Name: {first_name} {last_name}
    Email: {email_from}
    Phone: {phone}
    
    Message: 
    {message}
    """)

    mail = Mail(
        Email('notification@edmondchuc.com'), # the sender email
        subject,
        EMAIL_TO,
        content
    )
    response = sg.client.mail.send.post(request_body=mail.get())
    print(f'New email sent.\n'
          f'Status code: {response.status_code}'
          f'Body: {response.body}'
          f'Headers: {response.headers}')

    print(content.value)
    return 'Thank you for your message.'


@app.route('/', methods=['GET'])
def index():
    return 'Hello, World!'


@app.route('/test', methods=['POST', 'GET'])
def test():
    # from_email = Email("test@example.com")
    # to_email = Email("test2@example.com")
    # subject = "[www.edmondchuc.com] Sending with SendGrid is Fun"
    # content = Content("text/plain", "and easy to do anywhere, even with Python")
    # mail = Mail(from_email, subject, to_email, content)
    # response = sg.client.mail.send.post(request_body=mail.get())
    # print(response.status_code)
    # print(response.body)
    # print(response.headers)
    return 'API works!'

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()