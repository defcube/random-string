import io
import random


ALPHABET = ''.join([chr(x) for x in range(ord('a'), ord('z') + 1)]) + \
           ''.join([chr(x) for x in range(ord('A'), ord('Z') + 1)]) + \
           ''.join([str(x) for x in range(0, 10)])


def generate(min_length=12, max_length=18, alphabet=ALPHABET):
    """
    Generate a new random string

    >>> import random; random.seed(2)
    >>> generate(min_length=5, max_length=10)
    'ffx1k'
    >>> generate(min_length=5, max_length=10, alphabet='!@#')
    '#@@#!#!##!'


    :type min_length: int
    :type max_length: int
    :type alphabet: str
    :rtype: str
    """
    res = io.StringIO()
    for i in range(random.randint(min_length, max_length)):
        res.write(random.choice(alphabet))
    res.seek(0)
    return res.read()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
