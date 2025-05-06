from flask import Flask
import logging
app = Flask(__name__)
logging.basicConfig(filename='/logs/app.log', level=logging.INFO)

@app.route('/')
def hello_world():
    app.logger.info('Received a request!')
    return 'Hello World From Python App!'
if __name__ == '__main__':#
    app.run(host='0.0.0.0', port=5000)
