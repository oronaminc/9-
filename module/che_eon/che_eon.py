# 체언(명사, 대명사, 수사)을 다루는 모듈
from module.jamostoolkit import *
from .che_eon_list import *
from module.basic import namePumsa

def nameNoun(l):
    pumsalist = []
    for i in range(0, len(l)):
        if (isinstance(l[i], list)):
            continue
        word = l[i]
        check = JamosSeparator(word) #초성분리 모듈사용 (jamostoolkit)
        check.run() # 초성분리 동작
        chosung = check.get()[0] # 분리 결과값 받아오는 메서드
        if chosung == 'ㄱ':
            pumsalist = alist
        elif chosung == 'ㄴ':
            pumsalist = blist
        elif chosung == 'ㄷ':
            pumsalist = clist
        elif chosung == 'ㄹ':
            pumsalist = dlist
        elif chosung == 'ㅁ':
            pumsalist = elist
        elif chosung == 'ㅂ':
            pumsalist = flist
        elif chosung == 'ㅅ':
            pumsalist = glist
        elif chosung == 'ㅇ':
            pumsalist = hlist
        elif chosung == 'ㅈ':
            pumsalist = ilist
        elif chosung == 'ㅊ':
            pumsalist = jlist
        elif chosung == 'ㅋ':
            pumsalist = klist
        elif chosung == 'ㅌ':
            pumsalist = llist
        elif chosung is 'ㅍ':
            pumsalist = mlist
        elif chosung is 'ㅎ':
            pumsalist = nlist

        if l[i] in pumsalist:
            templist = [l[i], '명사']
            del l[i]
            l.insert(i, templist)
    return l

def processCheEon(l):
    l = namePumsa(l, susaList, '수사')
    l = namePumsa(l, daemyungsaList, '대명사')
    l = nameNoun(l)
    return l
