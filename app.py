from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/contact', methods=['POST'])
def contact():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    print(
        f'first name: {first_name}\n'
        f'last name: {last_name}\n'
        f'email: {email}\n'
        f'phone: {phone}\n'
        f'message: {message}'
    )
    return 'Thank you for your message.'


@app.route('/', methods=['GET'])
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
