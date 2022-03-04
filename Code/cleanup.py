from string import punctuation
import re
from tokens import tokenize

def read_file(markov):
    with open(markov) as f:
        text = f.read()
        punct = punctuation + '”“‘’–…'
        mod_str = ' '.join(filter(None, (word.strip(punct) for word in text.split())))
        low_str = mod_str.lower()
        str_list = re.sub('i\s', ' I ', low_str)
    return str_list

def clean_up(markov):
    with open(markov) as f:
        text = f.read()
        tokens = tokenize(text)
    return tokens

if __name__ == '__main__':
    print(read_file('code/script.txt'))