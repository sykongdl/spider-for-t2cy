import os
import re

os.chdir('t2cy')
rootpath = os.getcwd()


def chname(__name):
    __name = __name.lower()
    illegalchara = ['/', ':', '*', '?', '"', '<', '>', '|', '\\']
    for i in illegalchara:
        if __name.find(i) != -1:
            __name = __name.replace(i, '-')
    return __name


def gotocnfloder(cn):
    dirlist = os.listdir()
    if cn in dirlist:
        os.chdir(cn)
    else:
        os.mkdir(cn)
        os.chdir(cn)


def gotopackfolder(packname):
    dirlist = os.listdir()
    if packname in dirlist:
        cnt = 0
        for i in dirlist:
            if re.search(packname, i) is not None:
                cnt += 1
        packname = packname + '(' + str(cnt) + ')'
    os.mkdir(packname)
    os.chdir(packname)


def gotofolder(cn, packname):
    """
    walk to the cospack floder
    :param cn: coser name
    :param packname: img pack name
    :return: null
    """
    os.chdir(rootpath)
    gotocnfloder(chname(cn))
    gotopackfolder(chname(packname))


if __name__ == '__main__':
    gotofolder('Mokomo葵葵', '碧蓝航线能代/貅cos')