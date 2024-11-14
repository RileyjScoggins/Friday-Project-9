from dotenv import load_dotenv
import os

# Specify the correct path to the .env file for macOS
dotenv_path = "/Users/rileyscoggins/Desktop/DS3850/.env"
load_dotenv(dotenv_path)

# Debug: Check if the file is being loaded
if os.path.exists(dotenv_path):
    print(f".env file found at {dotenv_path}")
else:
    print(f".env file NOT found at {dotenv_path}")

# Retrieve the API key
api_key = os.getenv("OPENAI_API_KEY")

# Check if the key was loaded
if api_key:
    print("API Key loaded successfully.")
else:
    print("Failed to load API Key.")

