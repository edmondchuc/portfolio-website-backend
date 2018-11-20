# Portfolio Website Backend
## API
The website's API:
### Contact Form
`/api/contact`

### Test
`/api/test`

### GitHub Webhook
`/api/postreceive`
This webhook currently automatically copies the `index.html`, `static/css/*` and `static/img/*` to the Apache directories.
See this URL for more information. https://github.com/bloomberg/python-github-webhook 

## SendGrid Flask API
This is a very simple and extensible Flask application for sending emails via a RESTful API. 

Out of the box, the only thing required to change is to install the required modules and set up a simple configuration file. 

Additional routes can be easily created. An example `/contact` route has been created to show its simple usage

## Installation for SendGrid
Install the modules in `requirements.txt` and obtain a valid API key from [SendGrid](https://sendgrid.com).

Set environment variable `SENDGRID_API_KEY` to the API key obtained from your SendGrid account. Manually do this if you're using PyCharm in the `Edit Configurations` menu of the project.

Follow the instructions in configuration/copy_me.py file. It will instruct you to create a new file in the configuration directory.

Once you have created the new file from the instructions, set the configurations appropriate for your usage.

Run the application `app.py`.

## Installation for GitHub Webhook
Ensure that the bash scripts have correct permissions (744).

## Tests
Validation tests for the user configuration settings can be found in the `tests` directory.

## Notes
1. After every pull, set the bash script permissions.

## Contact
Edmond Chuc  
www.edmondchuc.com