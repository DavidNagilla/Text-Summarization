import _pickle as pickle
from os import path
from nltk.tokenize import word_tokenize

import config
import prep_data


def tokenize_sentence(sentence):
    return ' '.join(list(filter(
        lambda x: x.lower() != "advertisement",
        word_tokenize(sentence))))

def text_is_complete(r):
    if ('title' not in r) or ('instructions' not in r):
        return False
    if (r['title'] is None) or (r['instructions'] is None):
        return False
    return True

def tokenize(text):
    tokenized = []
    N = len(text)
    for i, r in enumerate(text.values()):
        if recipe_is_complete(r):
            desc = '; '.join(parse_ingredient_list(r['desc'])) + '; '
            tokenized.append((
                tokenize_sentence(r['title']),
                tokenize_sentence(desc) ))
        if i % 10000 == 0:
            print('Tokenized {:,} / {:,} text'.format(i, N))
    return tuple(map(list, zip(*tokenized)))

def pickle_text(text):
    # pickle to disk
    with open(path.join(config.path_data, 'tokens.pkl'), 'wb') as f:
        pickle.dump(recipes, f, 2)

def load_text():
    # pickle to disk
    with open(path.join(config.path_data, 'tokens.pkl'), 'rb') as f:
        text = pickle.load(f)
    return recipes

def main():
    text = prep_data.load_text()
    text_sum_data = tokenize_text(text)
    pickle_text(text_sum_data)

if __name__ == '__main__':
    main()
