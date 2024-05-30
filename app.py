import streamlit as st
import sys
import time
from io import StringIO
from threading import Thread

class StreamlitLogger:
    def __init__(self):
        self.log = StringIO()
        sys.stdout = self.log

    def get_logs(self):
        return self.log.getvalue()

# Create a StreamlitLogger instance
logger = StreamlitLogger()

# Print startup message
print("Application is starting up...")

# Sample function to generate logs
def generate_logs():
    for i in range(10):
        print(f"Log entry {i+1}: This is a sample log message.")
        time.sleep(1)  # Simulate time delay for log generation

# Function to update logs in Streamlit app
def update_logs():
    while True:
        logs = logger.get_logs()
        log_container.text_area("Log Output", logs, height=300, key="log_output")
        time.sleep(1)
        st.experimental_rerun()

# Streamlit app layout
st.title("Real-time Log Viewer")
st.write("### Logs:")
log_container = st.empty()  # Placeholder for the log output

# Button to start generating logs
if st.button("Start Logging"):
    # Start log generation in a separate thread
    Thread(target=generate_logs).start()
    # Start log updates in the main thread
    Thread(target=update_logs).start()
