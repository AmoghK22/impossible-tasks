from src.strings import slugify, titlecase
def test_slug():
    assert slugify("Hello World") == "hello-world"
def test_title():
    assert titlecase("hello world") == "Hello World"
