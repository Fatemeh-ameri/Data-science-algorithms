import operator
from collections import defaultdict
import pandas as pd

indivDict = defaultdict(int)
path = 'itcont.txt'

#Show the 20 first element 
df = pd.read_csv("itcont.txt", sep="|", header=None)
df1 = df[[0, 7, 14]]
print(df1.head(20))

with open(path) as f:            
    for string in f:             
        data = string.split("|") 
                                 
        indivDict[data[7]] += int(data[14])
        
print("Number of Records: ", len(indivDict))

"""output:
Number of Records:  947655"""

#BigToSmall
#sortedSums = sorted(indivDict.items(), key=operator.itemgetter(1), reverse=True)

#SmallToBig
sortedSums = sorted(indivDict.items(), key=operator.itemgetter(1))

TenMin = sortedSums[0:10]
n = 0
for item in TenMin:
    n += 1
    print("Least Helpful",{n}, item[1], item[0])

"""
output:
Least Helpful {1} -1185000 BROWN, MELISSA M
Least Helpful {2} -90000 MCCABE, MOLLY
Least Helpful {3} -32500 DISABLED AMERICAN VETERANS CHARITABLE SERVICE TRUST
Least Helpful {4} -30800 BERNSTORFF, MARGARET MRS
Least Helpful {5} -24600 SORRELL, MICHAEL E MR.
Least Helpful {6} -15340 ROSE, BERNARD
Least Helpful {7} -13000 MORRIS, ISAAC A
Least Helpful {8} -10400 ANDERSON, ROBERT F. MR.
Least Helpful {9} -10200 BRIGHAM, BEN BUD MADISON MR.
Least Helpful {10} -10000 LOCKHART, SUSAN
""" 

TenMax = sortedSums[-10:] 
n = 0   
for item in TenMax:
    n += 1
    print("Most Helpful",{n}, item[1], item[0])

"""
output:
Most Helpful {1} 6565000 AFL-CIO COPE TREASURY
Most Helpful {2} 7333600 SIMONS, JAMES H.
Most Helpful {3} 8104047 DEMOCRATIC GOVERNORS ASSOCIATION (DGA)
Most Helpful {4} 8746400 EYCHANER, FRED
Most Helpful {5} 10061929 ASSOCIATION OF REALTORS, NATIONAL
Most Helpful {6} 10801774 SINGER, PAUL
Most Helpful {7} 11795092 SENATE MAJORITY PAC
Most Helpful {8} 17974149 NATIONAL EDUCATION ASSOCIATION
Most Helpful {9} 23210529 BLOOMBERG, MICHAEL R.
Most Helpful {10} 73762600 STEYER, THOMAS F.
"""    
  
