def read_file(filename):
    f = open(filename, 'r', encoding='utf-8-sig')
    words = f.read()
    f.close()
    return words

def histogram(file):
    with open(file, 'r') as f:
        text = f.read().split()
        punctuation = '''!()-[]{};:'"\…,<>./?@#$%‼^&*_~”„“‥\n'''
        histogram = {}

        for word in text:
            for letter in word:
                if letter in punctuation:
                    word = word.replace(letter, "")
            if word in histogram.keys():
                histogram[word] += 1
            else:
                histogram[word] = 1
        return histogram

def unique_words(histogram):
    print("This text contains [" + str(len(histogram)) + "] unique words.")
    return len(histogram)

def frequency(word: str, histogram):
    if type(histogram) == dict:
        return histogram[word]
    else:
        for pair in histogram:
            if pair in histogram:
                if pair[0] == word:
                    return pair[1]

if __name__ == '__main__':
    histogram = histogram('code/script.txt')
    print(histogram)
    print(unique_words(histogram))
    print(frequency('Blocky', histogram))
    print(frequency('Bubble', histogram))
    print(frequency('Coiny', histogram))
    print(frequency('Eraser', histogram))
    print(frequency('Firey', histogram))
    print(frequency('Flower', histogram))
    print(frequency('Golf', histogram))
    print(frequency('Ball', histogram))
    print(frequency('Ice', histogram))
    print(frequency('Cube', histogram))
    print(frequency('Leafy', histogram))
    print(frequency('Match', histogram))
    print(frequency('Needle', histogram))
    print(frequency('Pen', histogram))
    print(frequency('Pencil', histogram))
    print(frequency('Pin', histogram))
    print(frequency('Rocky', histogram))
    print(frequency('Snowball', histogram))
    print(frequency('Spongy', histogram))
    print(frequency('Teardrop', histogram))
    print(frequency('Tennis', histogram))
    print(frequency('Woody', histogram))