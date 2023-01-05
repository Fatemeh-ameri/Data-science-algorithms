import operator

pathCm = 'cm.txt'
#key: committee identification codes
#calue: committee names
nameDict = {}
with open(pathCm, encoding="utf8") as f:
    for line in f:
        dataCm = line.split("|")
        if dataCm[1] != ' ':
            nameDict[dataCm[0]] = dataCm[1]
print("Number of committees = ", len(nameDict))
committees = set(nameDict.keys()) 
#print(committees)           

pathItoth = 'itoth.txt'
#key: committee identification codes
#value: set containing the names of the committees that have contributed to the committee
contributorDict = {}
with open(pathItoth, encoding="utf8") as f:
    for line in f:
        dataItoth = line.split("|")
        contributor = dataItoth[0]
        if contributorDict.get(contributor) is None:
            contributorDict[contributor] = {dataItoth[7]}
        else:
            contributorDict[contributor] = contributorDict[contributor].union({dataItoth[7]})
n = len(contributorDict)
print("N pairs = ", n*(n-1)/2)
#print(contributorDict.keys())
#print(contributorDict.values())            

for key in list(contributorDict.keys()):
    if len(contributorDict[key]) <= 500:
        contributorDict.pop(key, None)
n = len(contributorDict)        
print("N pairs = ", n*(n-1)/2)

for key in contributorDict:
    print(nameDict[key], len(contributorDict[key]))

contributor = list(contributorDict.keys())
print(contributor)   
pairs = [(contributor[i], contributor[j]) for i in range(n-1) for j in range(i+1, n, 1)] 
#print(pairs)

simDict = {}
#key: pairs(name of committees)
#value: determined 3-tuple similarity measures
for commA, commB in pairs:
    A = contributorDict[commA] #set of contributors to commA
    nameA = nameDict[commA]
    B = contributorDict[commB] #set of contributor to commB
    nameB = nameDict[commB]

    nIntersection = len(A.intersection(B))
    jAB = nIntersection/float(len(A.union(B)))
    pAGivenB = nIntersection/len(B)
    pBGivenA = nIntersection/len(A)

    simDict[(nameA, nameB)] = (jAB, pAGivenB, pBGivenA)
sortedList = sorted(simDict.items(), key=operator.itemgetter(1), reverse= True)

for committees, simMeasures in sortedList:
    nameA, nameB = committees
    jAB, pAB, pBA = simMeasures
    if jAB > .5:
        print(round(jAB, 3), round(pAB, 3), round(pBA, 3), nameA + ' | ' + nameB)

