import streamlit as st
import sys
import time

# Create a custom stream to capture stdout
class StdoutCapture:
    def __init__(self):
        self.buffer = ""
        self.original_stdout = sys.stdout

    def write(self, message):
        self.buffer += message
        if "\n" in message:
            self.flush()

    def flush(self):
        self.original_stdout.write(self.buffer)
        self.original_stdout.flush()
        self.buffer = ""

# Create an instance of the custom stream
stdout_capture = StdoutCapture()

# Redirect stdout to the custom stream
sys.stdout = stdout_capture

# Streamlit app layout
st.title("Real-time Log Viewer")
st.write("### Logs:")

# Function to continuously display logs
def display_logs():
    while True:
        # Get the captured logs
        logs = stdout_capture.buffer
        # Display logs in the Streamlit UI
        st.text(logs)
        # Clear the buffer to avoid duplication of logs
        stdout_capture.buffer = ""
        time.sleep(0.1)  # Adjust sleep time as needed

# Start displaying logs
display_logs()
