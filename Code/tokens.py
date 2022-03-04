import string

def tokenize(text):
    no_punc_text = remove_punctuation(text)
    tokens = split_on_whitespace(no_punc_text)
    return tokens

def split_on_whitespace(inputed_text):
    word_list = inputed_text.split()
    return word_list

def remove_punctuation(text):
    punct = string.punctuation
    for chars in text:
        if chars in punct:
            text = text.replace(chars, '')
    return text

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        source = open(filename).read()
        tokens = tokenize(source)
        print(tokens)
    else:
        print('No source text filename has been given as argument')