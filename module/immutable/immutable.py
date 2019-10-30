# 체언을 제외한 불변어(독립언(감탄사), 관계언(조사), 수식언(부사, 관형사))를 다루는 모듈
from module.basic import readPumsaData, namePumsa
from .immutableList import *

#리스트를 조사로 쪼개고 그 중 조사가 있으면 조사표시를 해줌
def divideAndNameJosa(josaList, l):
  josaListLength=len(josaList)
  '''lLength=len(l) 수정된 코드입니다.'''
  for i in range(josaListLength):
    josa = josaList[i]
    josaLength = len(josa)
    ''' 수정된 코드입니다. for j in range(lLength) -> for j in range(len(l))'''
    for j in range(len(l)):#나를 이름으로 불러줘
      word = l[j]#나를j=0
      if(len(word)<=josaLength or isinstance(word, list)):
        continue
      if(word[-josaLength:]==josa):#를
        beforeJosa = word[:-josaLength]#나
        del l[j]#이름으로 불러줘
        l.insert(j,beforeJosa)#나 이름으로 불러줘
        tempList=[josa,'조사']
        l.insert(j+1,tempList)#나 를 이름으로 불러줘
  return l

def processImmutable(l):
    l = namePumsa(l,gamtansaList, '감탄사')
    l = namePumsa(l,gwanhyeongsaList, '관형사')
    l = namePumsa(l,busaList, '부사')
    return l
