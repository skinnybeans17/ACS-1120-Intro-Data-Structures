import string

def open_file(inputed_text):
    file = open(inputed_text, 'r')
    text = file.read()
    file.close()
    return text

def lower_cased(inputed_text):
    text = inputed_text
    text = text.lower()
    return text

def open_and_low(inputed_text):
    open_text = open_file(inputed_text)
    text = lower_cased(open_text)
    return text