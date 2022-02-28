"""Main script, uses other modules to generate sentences."""
from flask import Flask
from histogram import read_file
from histogram import histogram
from dictogram import Dictogram

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.
    word_list = read_file('Code/script.txt')
    histogram = Dictogram(word_list)
    return histogram


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    words = histogram('Code/script.txt')
    return words
    #return "<p>Needle is very needy! *slap*</p>"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)

#create listogram
#write set_of_words
#create sentence
#remove repeated_words
#read listogram
#return