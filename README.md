# Installation
Install the modules in `requirements.txt` and obtain a valid API key from [SendGrid](https://sendgrid.com).

Set environment variable `SENDGRID_API_KEY` to the API key obtained from your SendGrid account. Manually do this if you're using PyCharm in the `Edit Configurations` menu of the project.

Ensure that an `email_to.txt` file exists containing the email address receiving the messages from the contact form.
The application will read from this file and set `EMAIL_TO` as the email address destination.

Run the application using `python app.py`.

# Contact
Edmond Chuc  
www.edmondchuc.com