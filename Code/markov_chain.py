from histogram import histogram, read_file
file = './code/script.txt'
word_list = read_file(file).replace(',', '').replace('.', '').replace('?', '').replace('"', '').replace('”', '').replace('’', '').replace('`', '').replace('!', '').replace('/', '').replace(';', '').replace(':', '').lower().split()

from dictogram import Dictogram

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
    markov_chain = dict_of_histograms_generator(word_list)
    tweet = tweet_generator(markov_chain)
    print(tweet)