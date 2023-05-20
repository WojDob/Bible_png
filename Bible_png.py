from string import digits, punctuation
from PIL import Image
import requests
import numpy

URL = "https://www.gutenberg.org/cache/epub/10/pg10.txt"
TXT_START = "*** START OF THE PROJECT GUTENBERG EBOOK THE KING JAMES BIBLE ***"
TXT_END = "*** END OF THE PROJECT GUTENBERG EBOOK THE KING JAMES BIBLE ***"


def extract_book_content(text, start_marker, end_marker):
    try:
        start = text.index(start_marker) + len(start_marker)
        end = text.index(end_marker)
        return text[start:end]
    except ValueError:
        return ""


def clean_text(text):
    remove_nonletters = str.maketrans("", "", punctuation + digits)
    return (
        text.replace("\\r", "")
        .replace("\\n", "")
        .replace("\\x", "")
        .translate(remove_nonletters)
        .lower()
    )


def compute_rgb(coded_word, num_unique_words):
    C = coded_word * numpy.floor((256 * 256 * 256) / num_unique_words)
    R = C // (256**2)
    G = (C // 256) % 256
    B = C % 256
    return [R, G, B]


def text_to_image(text):
    list_of_words = text.split()
    num_of_words = len(list_of_words)
    unique_words = set(list_of_words)
    num_unique_words = len(unique_words)

    coded_words = {word: i for i, word in enumerate(unique_words)}

    root = int(numpy.ceil(numpy.sqrt(num_of_words)))
    x = y = root
    data = numpy.zeros((x, y, 3), dtype=numpy.uint8)

    v = 0
    for i in range(x):
        for j in range(y):
            coded_word = coded_words[list_of_words[v]]
            data[i, j] = compute_rgb(coded_word, num_unique_words)
            v += 1
            if v == num_of_words:
                return data


response = requests.get(URL).content.decode("utf-8")
Bible = extract_book_content(response, TXT_START, TXT_END)
Bible = clean_text(Bible)
image = Image.fromarray(text_to_image(Bible))
image.save("BIBLE.png")
