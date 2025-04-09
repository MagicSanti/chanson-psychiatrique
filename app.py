import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to shift letters by a given number (Caesar Cipher)
def shift_letters(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            # Shift within alphabet (A-Z or a-z)
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(new_char)
        else:
            # If the character is not a letter, don't change it
            result.append(char)
    return ''.join(result)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            # Debugging: print all form data
            print("Form data:", request.form)

            original_text = request.form['original_text']  # This is where the error occurs
            shift = int(request.form['shift'])
            comparison_text = request.form['comparison_text']

            # Encrypt the original text using Caesar Cipher
            encrypted_text = shift_letters(original_text, shift)

            # Compare the comparison text with the encrypted text
            if comparison_text == encrypted_text:
                result_message = "Success! The text matches the encrypted lyrics."
            else:
                result_message = "Failure! The text does not match the encrypted lyrics."

            return render_template('index.html', result_message=result_message, encrypted_text=encrypted_text)

        except KeyError as e:
            print(f"Missing key: {e}")
            return f"Error: Missing key {e}"

    return render_template('index.html', result_message=None, encrypted_text=None)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))  # Render uses port 10000 by default
    app.run(host='0.0.0.0', port=port)
