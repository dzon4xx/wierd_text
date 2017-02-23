import copy
import random
import re


def random_permute(text):
    if len(set(text)) == 1:  # do not permute words consisting of the same characters
        return text
    text = list(text)
    perm_text = copy.copy(text)
    random.shuffle(perm_text)
    while perm_text == text:
        random.shuffle(perm_text)
    return ''.join(perm_text)


def encode(text, sep='\n---weird---\n'):

    matches = [match for match in re.finditer(r'\w+', text, re.U)]
    words = []
    if not matches:
        return ''.join((sep, text, sep, words))

    for match in matches:
        word_len = match.end() - match.start()
        if word_len > 3:  # process only words longer than 3 characters
            words.append(match.group())
            word_body = text[match.start()+1:match.end()-1]
            perm_word_body = random_permute(word_body)
            text = ''.join((text[0:match.start()+1], perm_word_body, text[match.end()-1:]))
    words.sort(key=str.lower)
    words = ' '.join(word for word in words)
    return ''.join((sep, text, sep, words))


def matching_word(perm_word, word_list):
    for index, word in enumerate(word_list):
        if len(word) == len(perm_word):
            if word[0] == perm_word[0]:
                if word[-1] == perm_word[-1]:
                    if set(perm_word) == set(word):
                        return index, word
    raise ValueError('Not found')


def decode(coded_msg, sep='\n---weird---\n'):

    coded_msg = coded_msg.split(sep)
    text = coded_msg[-2]
    words = coded_msg[-1].split()

    matches = [match for match in re.finditer(r'\w+', text, re.U)]

    for match in matches:
        perm_word = match.group()
        if len(perm_word) > 3:  # process only words longer than 3 characters
            index, word = matching_word(match.group(), words)
            del words[index]
            text = ''.join((text[0:match.start()], word, text[match.end():]))
    return text
