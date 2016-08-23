from urllib.request import urlopen
from pyquery import PyQuery as pq
# html5lib (можно вставлять lxml)


if __name__ == "__main__":
    r = urlopen("http://python.org")
    content = r.read()
    # можно вставлять элементы из lxml
    d = pq(content)
    a = []
    elements = d('.blog-widget ul li')
    # print(elements)
    for el in elements:
        obj = {}
        el = pq(el)
        obj['date'] = el('time').attr('datetime')
        obj['text'] = el('a').text()
        obj['href'] = el('a').attr('href')
        a.append(obj)
    print(a)
    # print(d('.blog-widget ul li time').attr('datetime'))
    # print(d('[disabled]'))
    # print(d('div:first'))
