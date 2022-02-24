from histogram import histogram, read_file
file = './code/pets.txt'
word_list = read_file(file).replace(',', '').replace('.', '').replace('?', '').replace('"', '').replace('”', '').replace('’', '').replace('`', '').replace('!', '').replace('/', '').replace(';', '').replace(':', '').lower().split()

from dictogram import Dictogram

def dict_of_histograms_generator(word_list):
    begin = word_list[0]
    dict_of_histograms = {}
    for i in range(len(word_list) - 2):
        word = word_list[i]
        next_word = word_list[i + 1]

        tup = tuple([word, next_word])
        final_word = tup[1]
        next_next_word = word_list[i + 2]

        if tup not in dict_of_histograms:
            histogram = Dictogram()
            histogram.add_count(next_next_word)
            dict_of_histograms[tup] = histogram
        else:
            dict_of_histograms[tup].add_count(next_next_word)
    return dict_of_histograms

def tweet_generator(markov_chain_dict):
    tweet = ''
    begin = next(iter(markov_chain_dict))[0]
    second_word = next(iter(markov_chain_dict))[1]
    tweet += begin + " " + second_word
    character_limit = 140

    while len(tweet) < character_limit:
        tweet_list = tweet.split()
        final_word = tweet_list[-1]
        final_final_word = tweet_list[-2]
        tup = tuple([final_final_word, final_word])
        final_word_histogram = markov_chain_dict[tup]
        next_word = final_word_histogram.sample()
        tweet += ' ' + next_word
    return tweet

if __name__ == '__main__':
    markov_chain = dict_of_histograms_generator(word_list)
    tweet = tweet_generator(markov_chain)
    print(tweet)

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue):
            return self.queue.pop(0)
        else:
            raise ValueError("Queue is empty. Can't dequeue.")