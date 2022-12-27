from collections import defaultdict
import pandas as pd

#candidate master file
#key = Committee code 9
#value = Political party 2
path = 'cn.txt'
canDict = defaultdict(str)
with open(path, encoding="utf8") as f:
    for line in f:
        data = line.split("|")
        canDict[data[9]] = data[2]
print("Number of candidate: ",len(canDict))
#Number of candidate:  4722

#committee master file
#key = Committee code 0
#value = Political party 10
path = 'cm.txt'
otherDict = defaultdict(str)
with open(path, encoding="utf8") as f:
    for line in f:
        data = line.split("|")
        otherDict[data[0]] = data[10]
print("Number of committee: ",len(otherDict))
#Number of committee:  14905

#indiviual master file
path = 'itcont.txt'
employerDict = defaultdict(list) #list of all employers trasaction
num_of_contributors = defaultdict(int)
with open(path, encoding="utf8") as f:
    totals = {'REP':0, 'DEM':0, 'Other':0}
    for line in f:
        data = line.split("|")
        party = canDict.get(data[0])
        if party is None:
            party = otherDict[data[0]]
        x = (party, int(data[14]))

        employer = data[11]
        if employer != '':
            value = employerDict.get(employer)
            if value is None:
                employerDict[employer] = [x]
            else:
                employerDict[employer].append(x)

        try:
            totals[party] += 1  #rep and dem added 
        except:
            totals['Other'] += 1  # any other party added
    num_of_contributors = totals

reduceDict = defaultdict(dict)
for key in employerDict:
    totals = {'REP':0, 'DEM':0, 'Other':0}
    for value in employerDict[key]:  #value = (party, amount)
        try:
            totals[value[0]] += value[1]   #sum of contribution to rep and dem
        except:
            totals['Other'] += value[1]    #sum of contribution to other
    reduceDict[key] = totals  #for example microsoft: {rep: 10000, dem:50000, other: 855200}

sum_rep_contributions = 0
sum_dem_contributions = 0
sum_other_contributions = 0
dem_supporter_counter = 0

for key in reduceDict:
    if reduceDict[key]["DEM"] > 0:
        dem_supporter_counter += 1
        #print("DEM SUPPORTER: ", key)
    sum_rep_contributions += reduceDict[key]["REP"]
    sum_dem_contributions += reduceDict[key]["DEM"]
    sum_other_contributions += reduceDict[key]["Other"]
        
print("total of REP: ", sum_rep_contributions)
#total of REP:  642144708

print("total of DEM: ", sum_dem_contributions)
#total of DEM:  572627363

print("total of Other: ", sum_other_contributions)
#total of Other:  1030039597

print("# of REP Contribuers: ", num_of_contributors['REP'])
# of REP Contribuers:  643937

print("# of DEM Contribuers: ", num_of_contributors['DEM'])
# of DEM Contribuers:  691523

print("# of Other Contribuers: ", num_of_contributors['Other'])
# of Other Contribuers:  856691

print('# of DEM Supporter: ', dem_supporter_counter)
# of DEM Supporter:  141430