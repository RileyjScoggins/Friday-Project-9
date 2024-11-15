# Friday-Project-9
# OpenAI Completion GUI

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

2. **Create a .env File**: The application requires an API key from OpenAI. You can get your API key by signing up at OpenAI.

    Once you have your API key, create a file named `.env` in the same directory as the script and add your OpenAI API key as follows:
`OPENAI_API_KEY=your_api_key_here`

3. **Running the Application**: After setting up the .env file, you can run the Python script. The application will open a window where you can enter a prompt, and the model's response will be displayed.
`python your_script_name.py`

Note: The `.env` file is used to load environment variables securely, so you don't expose your API key in the code.

## How it Works:
- The GUI has a text box where you can enter a prompt.
- When you click the button to submit the prompt, the application sends the prompt to the OpenAI API and displays the response.
- The response will appear in a separate text box below the input field.

## Troubleshooting
- **.env file not found:** Ensure the `.env` file is in the correct location (the same directory as the script).
- **API key not loaded:** Double-check that the API key is correctly set in the .env file and that there are no extra spaces or newlines.
License
 ```bash
    This project is open source. You are free to use, modify, and distribute it under the MIT License.""" 