from string import punctuation

def read_file(file):
    with open(file) as f:
        text = f.read()
        punct = punctuation + '”“‘’–…'
        mod_str = ' '.join(filter(None, (word.strip(punct) for word in text.split())))
        str_list = mod_str.lower().split()
    return str_list

if __name__ == '__main__':
    print(read_file('code/script.txt'))