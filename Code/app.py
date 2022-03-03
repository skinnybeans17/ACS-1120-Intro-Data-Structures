"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from histogram import read_file, histogram
from cleanup import read_file
from tokens import tokenize
from markov_chain_two import MarkovChain

file = 'code/script.txt'

app = Flask(__name__)
source = open(file).read()
tokens = tokenize(source)

@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.
    word_list = read_file(file)
    #histogram = Dictogram(word_list)
    markov_chain = MarkovChain(word_list, 15)
    return markov_chain

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    markov_chain = before_first_request()
    walk = markov_chain.walk_chain(50)
    list_to_str = ""
    for i in walk:
        list_to_str += f'{i} '
    return render_template('index.html', message=list_to_str)
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