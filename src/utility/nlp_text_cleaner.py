"A module contains text cleaning utility methods"

import re
import string
import html
import itertools

import nltk
import nltk.corpus
from nltk.corpus import stopwords
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

from autocorrect import Speller
from langdetect import detect


# intialize stopwords
nltk.download("stopwords")
# NLTK POS tagger
nltk.download("averaged_perceptron_tagger")


def split_into_sentences(text):
    """A method to split text into sentences

    Args:
        text (str): text data

    Returns:
        list: list of sentences
    """
    return sent_tokenize(text)


def split_into_words(text):
    """A method to split text into words

    Args:
        text (str): text data

    Returns:
        list: list of words
    """

    return word_tokenize(text)


def lower_case_text(text):
    """A method to convert text to lower case

    Args:
        text (str): text data

    Returns:
        str: lower case text
    """

    return text.lower()


def remove_punctuation(text):
    """A method to remove punctuations in a text

    Args:
        text (str): text data

    Returns:
        str: text without punctuations
    """

    text = " ".join(
        [
            word
            for word in word_tokenize(text)
            if word not in (string.punctuation)
        ]
    )
    return text


def remove_unicode(text):
    """A method to remove unicode characters ina text

    Args:
        text (str): text data

    Returns:
        str: text without unicode characters
    """

    text = re.sub(
        r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?",
        " ",
        text,
    )

    return " ".join(text.split())


def remove_leading_trailing_whitespaces(text):
    """A method to remove white spaces at the begining or end of text

    Args:
        text (str): text data

    Returns:
        str: text without white spaces at the begining or end
    """

    text = re.sub(r"^\s+|\s+$", "", text)
    return text


def remove_duplicate_whitespaces(text):
    """A method to remove  consecutive white spaces

    Args:
        text (str): text data

    Returns:
        str: text without duplicate white spaces
    """

    return " ".join(text.split())


def detect_language(text):
    """A method to detect language of text

    Args:
        text (str): text data

    Returns:
        str: language name
    """

    try:
        language = detect(text)
    except Exception as ex:
        print("language can not be detected", ex)
    return language


def correct_grammar(text):
    """A method to correct spelling of a text

    Args:
        text (str): text data

    Returns:
        str: Spelling corrected text
    """

    # One letter in a word should not be present more than twice in continuation
    text = "".join("".join(s)[:2] for _, s in itertools.groupby(text))
    spell_checker = Speller(lang="en")
    text = spell_checker(text)
    return text


def remove_stopwrods(text):
    """A method to remove stopwords from text

    Args:
        text (str): text data

    Returns:
        str: text without stopwords
    """

    stop = stopwords.words("english")
    text = " ".join(
        [word for word in word_tokenize(text) if word not in (stop)]
    )
    return text


def apply_stemming(text):
    """A method to apply stemming on text

    Args:
        text (str): text data

    Returns:
        str: text with stemming words
    """

    stemmer = PorterStemmer()
    text = " ".join([stemmer.stem(word) for word in word_tokenize(text)])
    return text


def apply_lammatization(text):
    """A method to apply lemmatization on text

    Args:
        text (str): text data

    Returns:
        str: text with lemmatized words
    """

    lemmatizer = WordNetLemmatizer()
    text = " ".join(
        [lemmatizer.lemmatize(word) for word in word_tokenize(text)]
    )
    return text


def remove_hashtags(text):
    """A method to remove hashtags in word
    Args:
        text (str): text data

    Returns:
        str: text without hashtags
    """

    text = re.sub(r"#", "", text)
    return text


def remove_hyperlinks(text):
    """A method to remove hyperlinks in text

    Args:
        text (str): text data

    Returns:
        str: text without hyperlinks
    """

    text = re.sub(r"https?:\/\/.\S+", "", text)
    return text


def clean_html_code(text):
    """A method to remove html entities like &apos; ,&amp; ,&lt; etc/

    Args:
        text (str):  text data

    Returns:
        str: text without html entities
    """
    text = html.unescape(text)
    return text


def replace_contraction(text):
    """A method to sreplace contractions like n't,'ll etc

    Args:
        text (str): text data

    Returns:
        str: text without contractions
    """
    apostrophe_dict = {
        "'s": " is",
        "n't": " not",
        "'m": " am",
        "'ll": " will",
        "'d": " would",
        "'ve": " have",
        "'re": " are",
    }

    # replace the contractions
    for key, value in apostrophe_dict.items():
        if key in text:
            text = text.replace(key, value)
    return text


def get_pos_tags(text):
    """A method to get POS tags of text

    Args:
        text (str): text data

    Returns:
        list: POS tags of text
    """

    tokens = nltk.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    return pos


def clean_single_sentence(text):
    """A default method to clean single sentence

    Args:
        text (str): text data

    Returns:
        text: cleaned sentence
    """
    text = replace_contraction(text)
    text = remove_duplicate_whitespaces(text)
    text = remove_unicode(text)
    text = remove_punctuation(text)
    return text


def clean_paragraph_to_sentences(paragraph):
    """A default method to get cleaned sentences from a paragraph

    Args:
        text (str): text data

    Returns:
        list: list of cleaned sentences
    """

    sentences = []
    for sentence in split_into_sentences(paragraph):
        sentences.append(clean_single_sentence(sentence))
    return sentences


def clean_paragraph(paragraph):
    """A default method to clean complete paragraph

    Args:
        text (str): text data

    Returns:
        str: cleaned text
    """

    sentences = []
    for sentence in split_into_sentences(paragraph):
        sentences.append(clean_single_sentence(sentence))
    return ".".join(sentences)
