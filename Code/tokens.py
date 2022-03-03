import re

def tokenize(text):
    no_punc_text = remove_punctuation(text)
    script_text = script(no_punc_text)
    decap_text = decapitalize(script_text)
    recap_text = recapitalize(decap_text)
    tokens = split_on_whitespace(recap_text)
    return tokens

def split_on_whitespace(text):
    split_text = re.split('\s+', text)
    return split_text

def remove_punctuation(text):
    no_punc_text = re.sub('[(),.!?-]', '', text)
    no_punc_text = re.sub('--', ' ', no_punc_text)
    no_punc_text = re.sub('\[[0-9]\]', '', no_punc_text)
    no_punc_text = re.sub('[”“‘’–…"]', '', no_punc_text)
    return no_punc_text

def script(text):
    script = re.sub('script', ' script ', text)
    return script

def recapitalize(text):
    recapitalize = re.sub('i\s', ' I ', text)
    recapitalize = re.sub('hd\s', ' HD ', recapitalize)
    return recapitalize

def decapitalize(text):
    decapitalize = re.sub(r'[A-Z]', lambda m: m.group(0).lower(), text)
    return decapitalize

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        source = open(filename).read()
        tokens = tokenize(source)
        print(tokens)
    else:
        print('No source text filename has been given as argument')