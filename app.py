from flask import Flask, render_template, request

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *
import configuration as conf
import tests.test_configuration as tests

# grab the SendGrid API key from the environment variable
sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

app = Flask(__name__)


def send_email_to_sendgrid(email_from, subject, email_to, content):
    mail = Mail(
        email_from,
        subject,
        email_to,
        content
    )
    response = sg.client.mail.send.post(request_body=mail.get())
    print(f'New email sent.\n'
          f'Status code: {response.status_code}'
          f'Body: {response.body}'
          f'Headers: {response.headers}')
    print(content.value)


@app.route('/contact', methods=['POST'])
def contact():
    # these will make up the content of the email
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email_from = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    # subject of the email
    subject = f'[{conf.WEBSITE_DOMAIN}] New message from {first_name}'

    content = Content(
        'text/plain',
        f"""
        New message received from the contact form at {conf.WEBSITE_DOMAIN}
        
        Sender's details:
        Name: {first_name} {last_name}
        Email: {email_from}
        Phone: {phone}
        
        Message:
        {message}    
        """
    )

    for email in conf.EMAIL_RECEIVERS:
        send_email_to_sendgrid(
            Email(conf.EMAIL_SENDER),
            subject,
            Email(email),
            content
        )

    return 'Thank you for your message.'


@app.route('/test', methods=['POST', 'GET'])
def test():
    return 'API works!'


if __name__ == '__main__':
    if tests.run() == 0:
        # TODO: add tests for sendgrid environment variable to ensure it is set.
        app.run(debug=conf.DEBUG)
