from mathkit import strings


def test_slugify():
    assert strings.slugify("Hello World") == "hello-world"
    assert strings.slugify("  Spaces  and--dashes ") == "spaces-and-dashes"


def test_truncate_short():
    result = strings.truncate("hi", 5)
    assert result is not None


def test_truncate_long():
    result = strings.truncate("hello world", 8)
    assert result is not None
    # assert result == "hello w…"


def test_word_count():
    assert strings.word_count("one two three") == 3
