# 가변어(용언(동사, 형용사))를 다루는 모듈
from .mutableList import *

def youngeonException(word):
    global youngeon_eomi_exceptList
    for item in youngeon_eomi_exceptList:
        L = len(item)
        if len(word) < L: continue

        if len(item) == 1:
            if ord(item[0]) == 12596:
                if ord(word[-1]) % 28 == 20: return True
            if ord(item[0]) == 12601:
                if ord(word[-1]) % 28 == 24: return True
            if ord(item[0]) == 12609:
                if ord(word[-1]) % 28 == 4: return True
            if ord(item[0]) == 12610:
                if ord(word[-1]) % 28 == 5: return True

        if word[-(L - 1):] == item[1:]:
            if ord(item[0]) == 12596:
                if ord(word[-L]) % 28 == 20: return True
            if ord(item[0]) == 12601:
                if ord(word[-L]) % 28 == 24: return True
            if ord(item[0]) == 12609:
                if ord(word[-L]) % 28 == 4: return True
            if ord(item[0]) == 12610:
                if ord(word[-L]) % 28 == 5: return True
    return False

def find_none_consonant(word):  # 받침 빼는 것
    temp_ord = ord(word)
    if temp_ord % 28 > 16:
        temp_ord -= ((temp_ord % 28) - 16)
    elif temp_ord % 28 < 16:
        temp_ord -= ((temp_ord % 28) + 12)
    return (chr(temp_ord))


def name_eogan_adj(eogan_adjList, l):  # 형용사 찾는 것
    L_adj = len(eogan_adjList)
    L = len(l)
    for i in range(L):
        word = l[i]
        if isinstance(word, list): continue
        Flag = False
        for j in range(L_adj):
            adj = eogan_adjList[j]
            if adj == '': continue
            adjL = len(adj)
            if len(word) < adjL: continue
            if adjL == 1 and len(word) != 1:
                if word[0] == adj: Flag = True
            else:
                if (ord(adj[-1]) >= 12593 and ord(adj[-1]) <= 12622):
                    temp = word[:adjL - 1] + jaem[(ord(word[adjL - 1]) - 0xAC00) // 21 // 28]
                    if temp == adj: Flag = True
                else:
                    if word[:adjL] == adj:
                        Flag = True
                    elif (word[:(adjL - 1)] + find_none_consonant(word[adjL - 1])) == adj:
                        Flag = True
            if Flag:
                del l[i]
                tempList = [word, '형용사']
                l.insert(i, tempList)
    return l


def name_eogan_verb(eogan_verbList, l):  # 동사 찾는 것
    L_verb = len(eogan_verbList)
    L = len(l)
    for i in range(L):
        word = l[i]
        if isinstance(word, list): continue
        Flag = False
        for j in range(L_verb):
            verb = eogan_verbList[j]
            if verb == '': continue
            verbL = len(verb)
            if len(word) < verbL: continue
            if verbL == 1 and len(word) != 1:
                if word[0] == verb: Flag = True
            else:
                if (ord(verb[-1]) >= 12593 and ord(verb[-1]) <= 12622):
                    temp = word[:verbL - 1] + jaem[(ord(word[verbL - 1]) - 0xAC00) // 21 // 28]
                    if temp == verb: Flag = True
                else:
                    if word[:verbL] == verb:
                        Flag = True
                    elif (word[:(verbL - 1)] + find_none_consonant(word[verbL - 1])) == verb:
                        Flag = True
            if Flag:
                del l[i]
                tempList = [word, '동사']
                l.insert(i, tempList)
    return l

def processMutable(l):
    l = name_eogan_adj(eogan_adjList, l)
    l = name_eogan_verb(eogan_verbList, l)
    return l


