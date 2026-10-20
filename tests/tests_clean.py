from src.clean import clean_text


def test_dehyphenation():
    assert clean_text("docu-\nment") == "document"


def test_whitespace_collapse():
    assert clean_text("hello   \n\n world") == "hello world"


def test_empty():
    assert clean_text("") == ""
