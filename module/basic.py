# txt파일 가공 및 정렬 / 품사 표시

def makeList():
    sentence = input('한국어 문장을 입력해주세요 : ')
    l = sentence.split()
    for i in range(len(l)):
      l[i] = l[i].replace(".","")
      l[i] = l[i].replace(",","")
      l[i] = l[i].replace("!","")
      l[i] = l[i].replace("?","")
      l[i] = l[i].replace("!","")
      l[i] = l[i].replace('"',"")
    return l

# 품사 txt 파일을 군더더기 없이 가공해 리스트에 저장
def readPumsaData(pumsa):
    with open('./DB/' + pumsa + '.txt', 'r', encoding='utf-8-sig') as pumsaData:
        pumsaList = pumsaData.read().splitlines()

    length = len(pumsaList)

    for i in range(length):
        pumsaList[i] = pumsaList[i].replace("-", "")
        if (pumsaList[i].count('(')):
            pumsaList[i] = pumsaList[i][:-4]

    return sortByLength(pumsaList)  # sortByLength 처리된 상태로 리턴하도록 수정

def readPumsaData2(pumsa):
    with open('./DB/' + pumsa + '.txt', 'r', encoding='utf-8-sig') as pumsaData:
        pumsaList = pumsaData.read().splitlines()

    length = len(pumsaList)

    for i in range(length):
        pumsaList[i] = pumsaList[i].replace("-", "")
        if (pumsaList[i].count('(')):
            pumsaList[i] = pumsaList[i][:-4]

    return sortByLength2(pumsaList)  # sortByLength2 처리된 상태로 리턴하도록 수정


#리스트 길이 긴순->짧은순 으로 정렬
def sortByLength(pumsaList):
  maxLength=0
  for pumsa in pumsaList:
    if maxLength < len(pumsa):
      maxLength=len(pumsa)
  tempList=[]
  for pLength in range(maxLength,0,-1):
    for pumsa in pumsaList:
      if len(pumsa) == pLength:
        tempList.append(pumsa)
  pumsaList=tempList
  return pumsaList

#리스트 길이 짧은순->긴순 으로 정렬
def sortByLength2(pumsaList):
  maxLength=0
  resultList = []
  for pumsa in pumsaList:
    if pumsa is None: continue
    if maxLength < len(pumsa):
      maxLength=len(pumsa)
  for pLength in range(maxLength):
    tempList = []
    for pumsa in pumsaList:
      if pumsa is None: continue
      if len(pumsa) == pLength:
        tempList.append(pumsa)
    tempList.sort()
    resultList.extend(tempList)
  return resultList


#리스트 중 특정 품사가 있으면 품사표시를 해줌
def namePumsa(l,pumsaList,pumsaType):
  for eojeol in l:
    if eojeol in pumsaList:
      tempList=[eojeol,pumsaType]
      idx=l.index(eojeol)
      del l[idx]
      l.insert(idx,tempList)
  return l

def left_process(l): # 아무것도 지정안된 것은 명사
  for idx in range(len(l)):
    if isinstance(l[idx], list): continue
    word = l[idx]
    del l[idx]
    tempList=[word,'명사']
    l.insert(idx,tempList)
  return l