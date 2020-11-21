import string

def is_pangram(sentence):
    """ 
    :param sentence: ASCII letters a to z, inclusive, and is case insensitive
    :return: True if sentence is pangram
    """

    chk = string.ascii_lowercase
    sentence = sentence.lower()
    for char in sentence:
        if char not in chk:
            return False
    return True


