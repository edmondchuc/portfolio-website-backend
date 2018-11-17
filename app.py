from flask import Flask

import configuration as conf
import tests.test_configuration as tests

from github_webhook import Webhook

from controller.contact_form import contact_form

app = Flask(__name__)
webhook = Webhook(app) # register GitHub webhook and define '/postreceive' endpoint
app.register_blueprint(contact_form)


@app.route('/test', methods=['POST', 'GET'])
def test():
    """
    Test that the website's API is working.
    :return:
    """
    return 'API works!'


@webhook.hook() # defines a handler for the 'push' event.
def on_portfolio_website_push(data):
    print(f'Received push with: {data}')


if __name__ == '__main__':
    if tests.run() == 0:
        app.run(debug=conf.DEBUG)
