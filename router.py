import importlib
import os
import json
from base_logger import get_logger

from flask import *
# from flask_cors import *
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from manager import app, dispatcher

# CORS(app, supports_credentials=True)


dm = DispatcherMiddleware(app, dispatcher)


if __name__ == '__main__':
    print(dispatcher)
    run_simple('0.0.0.0', int(os.environ.get('PORT', 80)), dm)