"""

Attention!
==========

Please create a new file named '__init__.py' in the current directory (configuration) and copy all the details in this
file to it.

Change the configurations to fit your purposes.

This file contains the configurations for this web API.

"""


# -*- coding: utf-8 -*-
#
# Configuration file for the backend service
# -------------------------------------------


# -- SendGrid API Settings ---------------------------------------------------------------------------------------------


SENDGRID_API_KEY = ''


# -- Contact Form API Settings -----------------------------------------------------------------------------------------

# These settings are used to configure the website's contact form API for SendGrid.

# The website domain containing the contact form.
WEBSITE_DOMAIN = ''

# The email of the sender as a string of characters.
EMAIL_SENDER = ''

# The list of emails of the receivers, each element as a string.
EMAIL_RECEIVERS = [

]


# -- Application Settings ----------------------------------------------------------------------------------------------

# Debug mode is on when True, change to False for production mode.
DEBUG = False
