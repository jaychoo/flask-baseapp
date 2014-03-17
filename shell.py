#!/usr/bin/env python
import os
import IPython

# Import our app
from app import *

os.environ['PYTHONINSPECT'] = 'True'

# Setup the IPython welcome message
welcome_message = """Welcome to your Flask CLI environment.
The following variables are available to use:

app -> Your Flask app instance
db -> Your Flask db instance
mail -> Your Flask mail instance
"""

# Start IPython
IPython.embed(header=welcome_message)