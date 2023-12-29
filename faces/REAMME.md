# Emoticon to Emoji Converter

A simple Python script that replaces emoticons with their corresponding emoji representations it's a CS_50 Project.

## Usage

The `playback` function takes user input and replaces emoticons with emojis using a predefined mapping.

### Example:

```python
from emoticon_to_emoji import playback

# Test cases
playback("Hello :)")        # Output: "Hello 🙂"
playback("Goodbye :(")      # Output: "Goodbye 🙁"
playback("Hello :) Goodbye :(")  # Output: "Hello 🙂 Goodbye 🙁"

How to Run

    Clone the repository:

    bash

git clone https://github.com/your-username/emoticon-to-emoji.git

Navigate to the project directory:

bash

cd emoticon-to-emoji

Run the script:

bash

    python playback.py

Emoticon to Emoji Mapping

The script uses the following mapping:

    :) is replaced with 🙂
    :( is replaced with 🙁
    :D is replaced with 😃
    ;) is replaced with 😉

Feel free to modify the emoji dictionary in the code to add more mappings as needed.
License

This project is licensed under the MIT License.
Author

Abanoub Ayad