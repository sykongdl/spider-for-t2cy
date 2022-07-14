import re
import requests

domin = r'https://t2cy.com'
cnre = re.compile(r'<h3 class.*?</h3>')
imgre1 = re.compile(r'<p><img.*?src=".*?"*?>')
imgre2 = re.compile(r'src=".*?"')
packnamere = re.compile(r'alt=".*?"')
packurlh3re = re.compile(r'<h3><a href=".*?" target="_blank" title=".*?">.*?</a></h3>')
packurlre = re.compile(r'href=".*?"')
nextpagere = re.compile(r'<a href="/acg/cos/index_.{1,2}.html">下一页</a>&nbsp;')
oldimgre = re.compile(r'http.*?://.*?')


def getpackinfo(contents):
    """
    :param contents:网页对象
    :return: infolist:(cn,packname,infolist)
    """
    imgrelist = imgre1.findall(contents.text)
    packname = packnamere.findall(imgrelist[0])
    cn = cnre.findall(contents.text)
    infolist = [cn[0][30:-5], packname[0][5:-1]]
    for __i in imgrelist:
        infolist += imgre2.findall(__i)
    for __i in range(2, len(infolist)):
        if oldimgre.findall(infolist[__i]):
            infolist[__i] = infolist[__i][5:-1]
        else:
            infolist[__i] = domin + infolist[__i][5:-1]
    print(infolist[0], infolist[1], len(imgrelist))
    return infolist


def getpackurl(contents):
    h3list = packurlh3re.findall(contents.text)
    h3list = h3list[3:]
    herflist = []
    urllist = []
    for __i in h3list:
        herflist += packurlre.findall(__i)
    for __i in herflist:
        urllist.append(domin + __i[6:-1])
    nextpageurlli = nextpagere.findall(contents.text)
    if nextpageurlli:
        nextpageurl = nextpageurlli[-1][9:-15]
        nextpageurl = domin + nextpageurl
        urllist.append(nextpageurl)
    else:
        urllist.append('eof')
    return urllist


if __name__ == '__main__':
    content = requests.get(r'https://t2cy.com/acg/cos/index_28.html')
    content.encoding = 'utf-8'
    packli = getpackurl(content)
    print(len(packli))
    for i in packli:
        print(i)