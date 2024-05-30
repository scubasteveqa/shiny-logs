import streamlit as st
import sys
import time
from io import StringIO

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

# Streamlit app layout
st.title("Real-time Log Viewer")

st.write("### Logs:")
log_container = st.empty()  # Placeholder for the log output

# Button to start generating logs
if st.button("Start Logging"):
    generate_logs()

# Continuously update the logs in the Streamlit app
while True:
    logs = logger.get_logs()
    log_container.text_area("Log Output", logs, height=300)
    time.sleep(1)
