import subprocess
import os

from flask import Blueprint, request
from github_webhook import Webhook

webhook_blueprint = Blueprint('webhooks', __name__)
webhook = Webhook(webhook_blueprint) # register GitHub webhook and define '/postreceive' endpoint

# Constants
GITHUB_WEBHOOK_BASH_SCRIPTS_PATH = './github_webhook_bash_scripts'


@webhook.hook() # defines a handler for the 'push' event.
def on_portfolio_website_push(data):
    """
    This route is called when GitHub's webhook makes a request with a JSON payload. It executes a bash script depending
    on the :code:`full_name` key's value in the JSON payload.

    :param data: GitHub JSON payload.
    :type data: JSON
    :return: None
    :rtype: None
    """
    full_name = data['repository']['full_name']
    print(f'Received push from: {full_name}')
    if full_name == 'edmondchuc/portfolio-website':
        subprocess.call(os.path.join(GITHUB_WEBHOOK_BASH_SCRIPTS_PATH, 'portfolio_asset_mv.sh'))
    elif full_name == 'edmondchuc/blog-site':
        subprocess.call(os.path.join(GITHUB_WEBHOOK_BASH_SCRIPTS_PATH, 'build-blog-and-deploy.sh'))

