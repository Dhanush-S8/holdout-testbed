from mathkit import strings


def test_slugify():
    assert strings.slugify("Hello World") == "hello-world"
    assert strings.slugify("  Spaces  and--dashes ") == "spaces-and-dashes"


def test_truncate_short():
    assert strings.truncate("hi", 5) == "hi"


def test_truncate_long():
    assert strings.truncate("hello world", 8) == "hello w…"


def test_word_count():
    assert strings.word_count("one two three") == 3
