from blog_travis_docker.__main__ import main


class TestMainFunc(object):
    def test_main_no_args(self, capsys):
        main(argv=[])

        out, err = capsys.readouterr()
        assert out == 'Hello!\n'
        assert err == ''

    def test_main_one_arg(self, capsys):
        main(argv=['World'])

        out, err = capsys.readouterr()
        assert out == 'Hello, World!\n'
        assert err == ''

    def test_main_multiple_args(self, capsys):
        main(argv=['Jamie', 'Hewland'])

        out, err = capsys.readouterr()
        assert out == 'Hello, Jamie Hewland!\n'
        assert err == ''
