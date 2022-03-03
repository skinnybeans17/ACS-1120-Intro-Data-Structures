from cleanup import read_file, clean_up
import random
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
                    words.append(self.corpus[index+i - len(self.__class__)])

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

    def walk_chain(self, word_count):
        str = []
        count = 0
        current = random.choice(self.corpus)
        print(current)
        while count in range(0, word_count):
            tuples = []
            for i in self.markov_dict.keys():
                if current == i[0]:
                    tuples.append(i)
                if len(tuples) == 0:
                    return str
                random_tuple = random.choice(tuples)
                for n in random_tuple:
                    str.append(n)
                    count += 1
                current = self.markov_dict[random_tuple].sample()
        return str

if __name__ == '__main__':
    test = MarkovChain(read_file('code/script.txt'), 10)
    print(test.walk_chain(25))