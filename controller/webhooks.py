import subprocess
import os

from flask import Blueprint, request
from github_webhook import Webhook

webhook_blueprint = Blueprint('webhooks', __name__)
webhook = Webhook(webhook_blueprint) # register GitHub webhook and define '/postreceive' endpoint

# Constants
GITHUB_WEBHOOK_BASH_SCRIPTS_PATH = './github_webhook_bash_scripts'


def get_full_name(data):
    """
    Return the full_name of the GitHub data object.

    :param data: GitHub data object as JSON.
    :type data: JSON
    :return: str
    :rtype: str
    """
    return data['repository']['full_name']


@webhook.hook() # defines a handler for the 'push' event.
def on_portfolio_website_push(data):
    """
    This route is called when GitHub provides a push from my portfolio-website repository.

    :param data: GitHub data object as JSON.
    :type data: JSON
    :return: None
    :rtype: None
    """
    full_name = get_full_name(data)
    print(f'Received push from: {full_name}')
    if full_name == 'edmondchuc/portfolio-website':
        subprocess.call(os.path.join(GITHUB_WEBHOOK_BASH_SCRIPTS_PATH, 'portfolio_asset_mv.sh'))


@webhook.hook()
def on_blog_site_push(data):
    """
    This route is called when GitHub provides a push from my blog-site repository.

    :param data: GitHub data object as JSON.
    :type data: JSON
    :return: None
    :rtype: None
    """
    full_name = get_full_name(data)
    print(f'Received push from: {full_name}')
    if full_name == 'edmondchuc/blog-site':
        subprocess.call(os.path.join(GITHUB_WEBHOOK_BASH_SCRIPTS_PATH, 'build-blog-and-deploy.sh'))