from bokeh.io import curdoc
from bokeh.models import Div
from threading import Thread
import sys
import time
from io import StringIO

class BokehLogger:
    def __init__(self):
        self.log = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.log

    def get_logs(self):
        return self.log.getvalue()

    def reset_stdout(self):
        sys.stdout = self.original_stdout

# Create a BokehLogger instance
logger = BokehLogger()

# Function to generate logs
def generate_logs():
    for i in range(10):
        print(f"Log entry {i+1}: This is a sample log message.")
        time.sleep(1)

# Define a Bokeh document
doc = curdoc()

# Create a Div to display logs
log_div = Div(width=800, height=400)

# Function to update log Div with real-time logs
def update_logs():
    while True:
        logs = logger.get_logs()
        log_div.text = logs
        time.sleep(1)

# Start generating logs in a separate thread
Thread(target=generate_logs).start()

# Start updating logs in a separate thread
Thread(target=update_logs).start()

# Add the log Div to the Bokeh document
doc.add_root(log_div)
