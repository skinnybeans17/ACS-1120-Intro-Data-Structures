from string import punctuation
import re
from tokens import tokenize

def read_file(file):
    with open(file) as f:
        text = f.read()
        punct = punctuation + '”“‘’–…'
        mod_str = ' '.join(filter(None, (word.strip(punct) for word in text.split())))
        low_str = mod_str.lower()
        recap_str = re.sub('i\s', ' I ', low_str)
        str_list = recap_str().split()
    return str_list

def clean_up(file):
    with open(file) as f:
        text = f.read()
        tokens = tokenize(text)
    return tokens

if __name__ == '__main__':
    print(read_file('code/script.txt'))