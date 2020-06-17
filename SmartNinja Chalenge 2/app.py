from flask import Flask, request, render_template

app = Flask(__name__)

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SHIFT_CHAR_NUMBER = 3


def rot13_encrypt(input_text=""):

    encrypt_string = input_text
    encrypted_string = ""

    for character in encrypt_string:

        tmp_char_poz = ALPHABET.find(character.upper())
        new_char = None

        if tmp_char_poz + SHIFT_CHAR_NUMBER + 1 > len(ALPHABET):
            new_char_poz = tmp_char_poz + SHIFT_CHAR_NUMBER - len(ALPHABET)
            new_char = ALPHABET[new_char_poz]
        else:
            if tmp_char_poz > -1:
                new_char_poz = tmp_char_poz + SHIFT_CHAR_NUMBER
                new_char = ALPHABET[new_char_poz]

        if new_char:
            if character == character.lower():
                new_char = new_char.lower()

            if character == character.upper():
                new_char = new_char.upper()

            encrypted_string = f"{encrypted_string}{new_char}"
        else:
            encrypted_string = f"{encrypted_string}{character}"

    return encrypted_string


@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == "POST":

        text_to_encrpyt = request.form.get('input_text')
        encrpyted_text = rot13_encrypt(text_to_encrpyt)

        return render_template('index.html', encrpyted_text=encrpyted_text)

    if request.method == "GET":

        return render_template('index.html')


if __name__ == '__main__':
    app.run()
