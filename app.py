import streamlit as st
import sys
import time
from io import StringIO
from threading import Thread

class StreamlitLogger:
    def __init__(self):
        self.log = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.log

    def get_logs(self):
        return self.log.getvalue()

    def reset_stdout(self):
        sys.stdout = self.original_stdout

# Create a StreamlitLogger instance
logger = StreamlitLogger()

# Function to generate logs
def generate_logs():
    for i in range(10):
        print(f"Log entry {i+1}: This is a sample log message.")
        time.sleep(1)

# Streamlit app layout
st.title("Real-time Log Viewer")
st.write("### Logs:")
log_container = st.empty()  # Placeholder for the log output

# Button to start generating logs
if st.button("Start Logging"):
    Thread(target=generate_logs).start()

# Update logs in real-time
while True:
    logs = logger.get_logs()
    log_container.text_area("Log Output", logs, height=300)
    time.sleep(1)
