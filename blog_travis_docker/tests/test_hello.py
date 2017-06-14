from blog_travis_docker.hello import hello


class TestHelloFunc(object):
    def test_hello(self):
        assert hello('World') == 'Hello, World!'

    def test_hello_no_name(self):
        assert hello(None) == 'Hello!'
