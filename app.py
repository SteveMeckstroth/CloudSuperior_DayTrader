import os

from flask import Flask

app = Flask(__name__)

TD_API_KEY = os.environ('TD_API_KEY')
print(TD_API_KEY)

@app.route('/')
def index():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
