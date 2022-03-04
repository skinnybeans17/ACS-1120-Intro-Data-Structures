from histogram import histogram, read_file
file = 'code/script.txt'
from cleanup import read_file
from tokens import tokenize
from dictogram import Dictogram
from random import randint, random
from tasks import open_and_low

def markov_chain(word_list):
    new_dict = {}
    for index in range(len(word_list) - 1):
        word = word_list[index]
        second_word = word_list[index +1]
        if word not in new_dict:
            add_word = Dictogram()
            add_word.add_count(second_word)
            new_dict[word] = add_word
        else:
            new_dict[word].add_count(second_word)
    return new_dict

def tweet_generator(markov, char_length):
    tweet = ''
    new_text = iter(markov)
    first_word = next(new_text)
    tweet += first_word
    char_limit = char_length
    while len(tweet) < char_limit:
        tweet_list = tweet.split()
        final_word = tweet_list[-1]
        final_word_histogram = markov[final_word]
        next_word = final_word_histogram.sample()
        tweet += ' ' + next_word
    return tweet

if __name__ == '__main__':
    file_text = open_and_low('code/script.txt')
    word_list = tokenize(file_text)
    markov_test = markov_chain(word_list)
    sentence_test = tweet_generator(markov_test, 60)
    print(sentence_test)