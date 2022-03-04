"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template, request, redirect
from markov_chain import markov_chain
from histogram import read_file, histogram
from cleanup import read_file
from tokens import tokenize
from markov_chain import tweet_generator
import twitter
from tasks import open_and_low

app = Flask(__name__)

file = open_and_low('code/script.txt')
tokenized_file = tokenize(file)
markov = markov_chain(tokenized_file)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    sentence = tweet_generator(markov, 80)
    return render_template('index.html', sentence=sentence)
    #return "<p>Needle is very needy! *slap*</p>"

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')

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