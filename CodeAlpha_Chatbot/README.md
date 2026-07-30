# Basic Rule-Based Chatbot

A simple rule-based chatbot built in Python as part of my internship at **CodeAlpha**. The bot responds to predefined user inputs using conditional matching, simulating a basic conversational flow.

##  About the Project

This chatbot works by checking user input against a set of hardcoded phrases and returning an appropriate scripted response. It's a beginner-friendly introduction to how rule-based conversational agents work before moving on to more advanced NLP-based or ML-based chatbots.

##  Features

- Responds to greetings (`hi`, `hello`)
- Simulates small talk (`how are you?`)
- Follows a simple scripted conversation flow (student → major → consultation)
- Exits gracefully when the user types `bye`
- Case-insensitive input handling

##  How It Works

The chatbot uses a function, `chatbot_responses()`, which:
1. Converts user input to lowercase for consistent matching
2. Compares it against a series of `if-elif` conditions
3. Returns a matching response, or a fallback message if no match is found

The main program runs an infinite loop that:
- Prompts the user for input
- Passes it to `chatbot_responses()`
- Prints the bot's reply
- Breaks the loop when the user types `bye`

##  Installation

1. Clone this repository or download `chatbot.py`:
```bash
git clone https://github.com/mjcodes-77/codealpha_tasks.git
cd codealpha_tasks/CodeAlpha_Chatbot
```
2. Make sure you have Python 3 installed:
```bash
python --version
```
3. No additional packages are required — the project uses only Python's standard library.

## ▶ Usage

Run the script with Python:

```bash
python chatbot.py
```

Then start chatting with the bot. Example conversation:

```
Welcome to the Chatbot
You: hi
Bot:  Hello!
You: how are you?
Bot:  I am fine. Thanks! What about you?
You: i am fine too.
Bot:  What do you do?
You: bye
Bot:  Have a nice day. Good bye!
```

**Note:** Since matching is exact, inputs must closely match the expected phrases (including punctuation) to get a scripted response. Anything else triggers the fallback: *"Sorry. I dont understand it."*

##  Requirements

- Python 3.14.2 (no external libraries needed)

##  Future Improvements

- Keyword-based matching instead of exact string matching for more natural conversations
- Punctuation stripping for more flexible input handling
- Conversation state tracking for more dynamic flows
- Integration of basic NLP (e.g., using `difflib` for fuzzy matching)

##  Acknowledgements

This project was completed as part of my internship with **[CodeAlpha](https://www.codealpha.tech/)**.

##  Author

**Malaika Jabeen**
GitHub: [@mjcodes-77](https://github.com/mjcodes-77)
