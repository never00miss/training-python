"""
This script runs the Sparse application using a development server.
"""

from os import environ
from Sparse import app

app.run('0.0.0.0', 6990, debug=True, threaded=True)
