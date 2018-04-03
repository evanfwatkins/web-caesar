from flask import Flask, request, render_template 
from caesar import rotate_string
from caesar import alphabet_position


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action= "/encrypt" method= "post">
            <label for="rot">Rotate by:</label>
            <input id="rot" type="text" name="rot" value=0 />
            <textarea id="text" name="text">{0}</textarea>
            <input type="submit"/>
    </body>
</html>
"""
@app.route("/") 
def index():
    return form.format("")

@app.route ("/encrypt", methods=["POST"])
def encrypt():
    text = request.form["text"]
    rot = request.form["rot"]
    rot = int(rot)
    new_encrypt = rotate_string(text, rot)
    return form.format(new_encrypt)

app.run()