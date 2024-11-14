import tkinter as tk
from dotenv import load_dotenv
import openai
import os

# Specify the path to the .env file
dotenv_path = "/Users/rileyscoggins/Desktop/DS3850/.env"
load_dotenv(dotenv_path)

# Debug: Check if the .env file is being loaded
if os.path.exists(dotenv_path):
    print(f".env file found at {dotenv_path}")
else:
    print(f".env file NOT found at {dotenv_path}")

# Load the OpenAI API key from the .env file
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key was loaded correctly
if api_key:
    openai.api_key = api_key
    print("API Key loaded successfully.")
else:
    print("Failed to load API Key.")

# Define the function to handle completion requests to OpenAI API
def get_completion():
    prompt = prompt_entry.get("1.0", tk.END).strip()  # Get prompt text from the user
    if prompt:
        try:
            # Make a request to the OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100
            )
            # Display the response in the output text box
            output_text.delete("1.0", tk.END)  # Clear any previous output
            output_text.insert(tk.END, response.choices[0].message['content'].strip())
        except Exception as e:
            output_text.delete("1.0", tk.END)  # Clear output
            output_text.insert(tk.END, f"Error: {e}")  # Show error message

# Set up the main application window
app = tk.Tk()
app.title("OpenAI Completion GUI")
app.geometry("500x400")

# Create prompt entry label and text box
prompt_label = tk.Label(app, text="Enter your prompt:")
prompt_label.pack(pady=5)

prompt_entry = tk.Text(app, height=5, width=50)
prompt_entry.pack(pady=5)

# Create submit button to send the prompt to OpenAI API
submit_button = tk.Button(app, text="Submit", command=get_completion)
submit_button.pack(pady=5)

# Create output label and text box to display the response
output_label = tk.Label(app, text="Output:")
output_label.pack(pady=5)

output_text = tk.Text(app, height=10, width=50)
output_text.pack(pady=5)

# Run the application
app.mainloop()
