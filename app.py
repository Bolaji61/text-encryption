from flask import Flask, render_template, request
import random

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

#generates shift number
def shift_number():
    for i in range(1):
        s = random.randint(1, 10)
    return s

# encrypt a text
@app.route('/encrypt', methods = ['POST'])
def encrypt():
    text = request.form.get('encrypt')     #read text from index.html
    s = shift_number()
    encrypted_text = ""

    # convert the plain text to encrypted form
    for i in range(len(text)):
        char = text[i] 
        
        if(char.isdigit() == True):
            raise ValueError("Digits not allowed")
            break
        else:
        # Encrypts upper case characters
            if (char.isupper()):
                encrypted_text += chr((ord(char) + s - 65) % 26 + 65)   #Generates a new character, also accounts for new ascii codes that are out of alphabet range
            # Encrypts lower case characters
            else:
                encrypted_text += chr((ord(char) + s - 97) % 26 + 97)

    return render_template("encrypt.html", encrypted_text = encrypted_text)


# decrypt an encrypted text
@app.route('/decrypt', methods = ['POST'])
def decrypt():
    ciphertext = request.form.get('decrypt')
    shift = int(request.form.get('shift_value'))
   

    # create a list of encrypted words.
    ciphertext = ciphertext.split()

    # creat a list to hold decrypted words.
    decrypted_text = []

    for char in ciphertext:
        cipher_ords = [ord(i) for i in char ]
        text_ords = [j - shift for j in cipher_ords]
        text_chars = [chr(k) for k in text_ords]
        text = ''.join(text_chars)
        decrypted_text.append(text)

    # join each word in the sentence list back together by a space.
    decrypted_text = ' '.join(decrypted_text)
    return render_template("decrypt.html", decrypted_text = decrypted_text)


if __name__ == "__main__":
    app.run(debug=True)

