from urllib.request import urlopen
from lxml import etree
# import lxml


if __name__ == "__main__":
    r = urlopen("http://python.org")
    content = r.read()
    # lxml.html.parse
    root = etree.HTML(content)
    # print(root.xpath('//div'))
    d = root.xpath('//a')
    # print(d[0].text)
    # print(d[0].attrib)
    # print(d[0].attrib['href'])
    # print(root.xpath('// a/text()'))
    a = []
    # a.append(root.xpath('/div'))
    element = root.xpath('//div[contains(@class, "blog-widget")]/div/ul/li')
    for el in element:
        obj = {}
        obj['date'] = el.xpath('.//time')[0].attrib['datetime']
        obj['text'] = el.xpath('.//a/text()')
        obj['href'] = el.xpath('.//a')[0].attrib['href']
        a.append(obj)
    print(a)
    # elem_li = root.xpath('ul/li')
