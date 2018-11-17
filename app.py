from flask import Flask

import configuration as conf
import tests.test_configuration as tests

from controller.contact_form import contact_form
from controller.webhooks import webhook_blueprint

app = Flask(__name__)
app.register_blueprint(contact_form)
app.register_blueprint(webhook_blueprint)


@app.route('/test', methods=['POST', 'GET'])
def test():
    """
    Test that the website's API is working.
    :return:
    """
    return 'API works!'


if __name__ == '__main__':
    if tests.run() == 0:
        app.run(debug=conf.DEBUG)
