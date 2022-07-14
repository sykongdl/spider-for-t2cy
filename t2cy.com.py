import requests
import RePack
import OsPack
from time import sleep
localurl = r'https://t2cy.com'
header = {
    'user-agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    "Connection": "close"
}


def downloadpack(packurl):
    # 获取网页，更改编码为utf-8
    content = requests.get(packurl)
    content.encoding = 'utf-8'
    # 获取cn，图包名称， 图片url
    cn, packname, *imgurls = RePack.getpackinfo(content)
    # 打包下载
    OsPack.gotofolder(cn, packname)  # 建立目录，并将工作区移至目录下
    # 开始下载
    cnt = 0  # 本包下载计数
    for imgurl in imgurls:
        cnt += 1
        with open(str(cnt)+'.jpg', 'wb') as f:
            f.write(requests.get(imgurl,headers=header).content)
    # 下载完成 返回工作区


def traversecos(packurl=r'https://t2cy.com/acg/cos/'):
    content = requests.get(packurl)
    content.encoding = 'utf-8'
    *packurllist, nextpageurl = RePack.getpackurl(content)
    for url in packurllist:
        try:
            downloadpack(url)
        except Exception as e:
            print(url)
            print(e.__class__.__name__, e)
            input('err')
        sleep(2)
    return nextpageurl


if __name__ == '__main__':
    nextpage = r'https://t2cy.com/acg/cos/index_25.html'
    while nextpage != 'eof':
        nextpage = traversecos(nextpage)
    print('finish')





