from histogram import histogram, read_file
file = 'code/script.txt'
word_list = read_file(file).replace(',', '').replace('.', '').replace('?', '').replace('"', '').replace('”', '').replace('’', '').replace('`', '').replace('!', '').replace('/', '').replace(';', '').replace(':', '').lower().split()

from dictogram import Dictogram

class MarkovChain(object):
    def __init__(self, word_list, order):
        super(MarkovChain, self).__init__()
        self.corpus = word_list
        self.dict = {}
        self.markov_dict = self.markov_chain(order)

    def markov_chain(self, order):
        word_tuples = []
        for index in range(0, len(self.corpus) - 1):
            words = []

            for i in range(0, order):
                if index+i in range(0, len(self.corpus)):
                    words.append(self.corpus[index+i])
                else:
                    words.append(self.corpus[index+i - len(self.corpus)])

            word_tuple = tuple(words)
            word_tuples.append(word_tuple)

            if index+order in range(0, len(self.corpus)):
                next_word = self.corpus[index+order]
            else:
                next_word = self.corpus[index+order - len(self.corpus)]

            if word_tuple in self.dict.keys():
                dictogram = self.dict[word_tuple]
                if next_word:
                    if next_word in dictogram.keys():
                        dictogram.add_count(next_word)
                    else:
                        dictogram.add_count(next_word)
            else:
                if next_word:
                    self.dict[word_tuple] = Dictogram([next_word])
        return self.dict

    def dict_of_histograms_generator(word_list):
        begin = word_list[0]
        dict_of_histograms = {}
        for i in range(len(word_list) - 1):
            word = word_list[i]
            next_word = word_list[i + 1]
            if word not in dict_of_histograms:
                histogram = Dictogram()
                histogram.add_count(next_word)
                dict_of_histograms[word] = histogram
            else:
                dict_of_histograms[word].add_count(next_word)
        return dict_of_histograms

    def tweet_generator(markov_chain_dict):
        tweet = ''
        begin = next(iter(markov_chain_dict))
        tweet += begin
        character_limit = 140

        while len(tweet) < character_limit:
            tweet_list = tweet.split()
            final_word = tweet_list[-1]
            final_word_histogram = markov_chain_dict[final_word]
            next_word = final_word_histogram.sample()
            tweet += ' ' + next_word
        return tweet

if __name__ == '__main__':
    test = MarkovChain(read_file('code/script.txt'), 10)
    print(test.markov_chain(25))