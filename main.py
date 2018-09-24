from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="" method="post">
            <label for="rot">Rotate by:
                <input type="text" name="rot" id="rot" value="0">
            </label>
            <textarea name="text" id="" cols="30" rows="10"></textarea>
            <input type="submit" value="Encrypt">
        </form>

    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rotation = request.form['rot']
    rotation = int(rotation)
    message = request.form['text']

    encrypted_message = rotate_string(message, rotation)

    return "<h1>" + encrypted_message + "</h1>"


app.run()
