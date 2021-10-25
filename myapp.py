from flask import Flask, render_template
import os
import random
app = Flask(__name__)
def random_jaden_quote():
    """
    return a random quote from Jaden Smith
    """
    quotes = [
        "Instagram is not the answer.",
        "You can discover everything you need to know about everything by looking at your hands",
        "Being born was the most influential thing that’s ever happened to me, for myself.",
        "When Life Gives You Big Problems, Just Be Happy You Forgot All Your Little Problems.",
        "The Lack Of Emotion In My Face Doesn't Mean I'm Unhappy.",
        "When The First Animal Went Extinct That Should've Been A Sign.",
        "How Can Mirrors Be Real If Our Eyes Aren't Real."
    ]
    quote = "%s -- Jaden Smith" % random.choice(quotes)
    return quote

@app.route('/')
def myapp():
    quote = random_jaden_quote()
    return render_template('index.html', random_quote=quote)