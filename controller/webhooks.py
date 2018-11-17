import subprocess

from flask import Blueprint, request
from github_webhook import Webhook

webhook_blueprint = Blueprint('webhooks', __name__)
webhook = Webhook(webhook_blueprint) # register GitHub webhook and define '/postreceive' endpoint


@webhook.hook() # defines a handler for the 'push' event.
def on_portfolio_website_push(data):
    full_name = data['repository']['full_name']
    print(f'Received push from: {full_name}')
    if full_name == 'edmondchuc/portfolio-website':
        subprocess.call('./github_webhook_bash_scripts/portfolio_asset_mv.sh')