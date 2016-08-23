from urllib.request import urlopen
from bs4 import BeautifulSoup


def index():
    r = urlopen("http://python.org")
    content = r.read()
    bs = BeautifulSoup(content, "html.parser")
    # print(bs.ul)
    # print(bs.find_all("a"))
    # print(bs.form)
    # print(bs.a['href'])
    # print(bs.p.text)
    return bs.find(
        'div',
        attrs={'id': 'success-story-2'}
    ).prettify()


if __name__ == "__main__":
    b = index()
    print(b)
