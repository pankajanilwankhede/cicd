from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, CI CD with git hub actions!"  # This should be visible in the browser.

if __name__ == '__main__':
    app.run(debug=True)


