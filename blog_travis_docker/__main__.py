import sys

from blog_travis_docker.hello import hello


def main(argv=sys.argv[1:]):
    print(hello(' '.join(argv)))


if __name__ == '__main__':
    main()
