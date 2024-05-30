from bokeh.io import curdoc
from bokeh.models import Div
from threading import Thread
import time
from io import StringIO
import sys

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

# Function to print environment setup logs
def print_environment_setup_logs():
    print("Starting environment setup...")
    # Simulate environment setup logs
    for i in range(5):
        print(f"Setting up environment step {i+1}...")
        time.sleep(1)
    print("Environment setup completed.")

# Function to update log Div with real-time logs
def update_logs():
    while True:
        logs = logger.get_logs()
        log_div.text = logs
        time.sleep(1)

# Define a Bokeh document
doc = curdoc()

# Create a Div to display logs
log_div = Div(width=800, height=400)

# Start printing environment setup logs in a separate thread
Thread(target=print_environment_setup_logs).start()

# Start updating logs in a separate thread
Thread(target=update_logs).start()

# Add the log Div to the Bokeh document
doc.add_root(log_div)
