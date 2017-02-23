import pytest

from weird_text import matching_word, random_permute, encode, decode


def test_should_find_matching_word_when_word_in_list():
    # GIVEN
    word = 'sentence'
    perm_word = 'sneetcne'
    words = [word, 'dog', '88888888', 'thisisis']
    # when
    index, found_word, = matching_word(perm_word, words)
    assert index == 0
    assert word == found_word


def test_should_raise_exception_word_not_in_list():
    # GIVEN
    perm_word = 'sneetcne'
    words = ['car', 'dog', '88888888', 'thisisis']
    # when
    with pytest.raises(ValueError):
        matching_word(perm_word, words)


def test_should_permute_word():
    # GIVEN
    word = 'artefact'
    perm_word = random_permute(word)

    assert len(word) == len(perm_word)
    assert set(word) == set(perm_word)


def test_random_permute_should_not_return_same_word():
    # GIVEN
    word = 'the'
    # WHEN
    for i in range(100):
        perm_word = random_permute(word)
        # THEN
        assert perm_word != word


def test_random_permute_should_return_same_word_when_word_consists_of_the_same_characters():
    # GIVEN
    word = 'iiiii'
    # WHEN
    perm_word = random_permute(word)
    # THEN
    assert perm_word == word


def test_encode_decode_text():
    # given
    test_text = 'This is a long looooong test sentence,\nwith some big (biiiiig) words!'
    # when
    encoded_text = encode(test_text)
    print(encoded_text)
    decoded_text = decode(encoded_text)
    # then
    assert decoded_text == test_text


def test_encode_decode_text1():
    # given
    test_text = 'This is a ążźća a a RaNdomly\n\n\n #Chosen wiiieerd words a ' \
                'long looooong test sentence,\nwith some big (biiiiig) words!'
    # when
    encoded_text = encode(test_text)
    print(encoded_text)
    decoded_text = decode(encoded_text)
    # then
    assert decoded_text == test_text
