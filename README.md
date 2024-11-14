# Friday-Project-9
readme_content = """# OpenAI Completion GUI

**IMPORTANT: You will need a `.env` file with your own OpenAI API key to run this project. Please follow the setup instructions below to configure it.**

This is a simple graphical user interface (GUI) application that interacts with OpenAI's GPT-3.5 model to generate text completions. The application takes a user prompt, sends it to the OpenAI API, and displays the model's response in a text box.

## Requirements

- Python 3.x
- `tkinter` for the GUI
- `openai` for API integration
- `python-dotenv` for managing environment variables

## Setup Instructions

1. **Install Dependencies**:
   You need to install the necessary Python libraries. You can do this using `pip`:

   ```bash
   pip install openai python-dotenv

**Create a .env File**: The application requires an API key from OpenAI. You can get your API key by signing up at OpenAI.
Once you have your API key, create a file named ```bash 
    .env 
in the same directory as the script and add your OpenAI API key as follows: