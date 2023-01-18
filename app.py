from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<title>Hello</title>
</head>
<body><h1>World</h1></body>
</html>"""
