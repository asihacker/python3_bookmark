from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    params = request.args or request.json  # GET
    print(params)
    return 'Hello World'


if __name__ == '__main__':
    app.run(port=39007, debug=True)
    