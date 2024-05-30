import sys
from io import StringIO
from threading import Thread
from shiny import App, render, ui

class ShinyLogger:
    def __init__(self):
        self.log = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.log

    def get_logs(self):
        return self.log.getvalue()

    def reset_stdout(self):
        sys.stdout = self.original_stdout

# Create a ShinyLogger instance
logger = ShinyLogger()

# Function to print environment setup logs
def print_environment_setup_logs():
    print("Starting environment setup...")
    # Simulate environment setup logs
    for i in range(5):
        print(f"Setting up environment step {i+1}...")
    print("Environment setup completed.")

# Function to print variables being loaded
def print_variables_loading_logs():
    print("Loading variables...")
    # Simulate loading variables logs
    variables = {"var1": 10, "var2": "Hello", "var3": [1, 2, 3]}
    for key, value in variables.items():
        print(f"Variable '{key}': {value}")
    print("Variable loading completed.")

# Define the Shiny UI
app_ui = ui.page_fluid(
    ui.h2("Real-time Log Viewer"),
    ui.output_text_area("log_output", rows=20, cols=80),
    ui.input_action_button("start_logging", "Start Logging")
)

# Define the Shiny server logic
def server(input, output, session):
    def update_logs():
        while True:
            logs = logger.get_logs()
            session.send_input_message("log_output", logs)
            time.sleep(1)

    @session.on_input_change("start_logging")
    def on_start_logging():
        if input.start_logging > 0:  # Check if the button is pressed
            Thread(target=print_environment_setup_logs).start()
            Thread(target=print_variables_loading_logs).start()
            Thread(target=update_logs).start()

app = App(app_ui, server)

# Run the app
if __name__ == "__main__":
    app.run()
