import logging
from flask import Flask

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
_log = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/')
def hello_world():
    _log.info('hello_world() called.')
    return 'Hello, World!'