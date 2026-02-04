from flask import Flask, request, jsonify

app = Flask(__name__)


def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result


def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result


@app.route("/process", methods=["POST"])
def process():
    data = request.json

    text = data.get("message", "")
    mode = data.get("mode", "encrypt")
    shift = int(data.get("shift", 3))

    if mode == "encrypt":
        result = encrypt(text, shift)
    else:
        result = decrypt(text, shift)

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
