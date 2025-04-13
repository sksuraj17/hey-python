from flask import Flask, jsonify
from datetime import datetime
import platform
import random
import sys

app = Flask(__name__)

quotes = [
    "Code is like humor. When you have to explain it, it’s bad.",
    "In a world without fences and walls, who needs Gates and Windows?",
    "First, solve the problem. Then, write the code.",
    "Experience is the name everyone gives to their mistakes.",
    "Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Monday’s code."
]

@app.route('/')
def hello():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <html>
        <head><title>Welcome</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h1>👋 Hey, there!</h1>
            <p>Current server time is: <strong>{now}</strong></p>
            <p><a href="/info">Check out system info</a></p>
            <p><a href="/quote">Get a random quote</a></p>
        </body>
    </html>
    """

@app.route('/info')
def system_info():
    info = {
        "python_version": sys.version,
        "platform": platform.system(),
        "platform_release": platform.release(),
        "architecture": platform.machine()
    }
    return jsonify(info)

@app.route('/quote')
def random_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
