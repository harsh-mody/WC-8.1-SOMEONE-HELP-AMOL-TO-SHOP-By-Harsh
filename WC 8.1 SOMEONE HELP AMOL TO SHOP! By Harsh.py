b = int(input("Please Enter Amol's Budget : "))
n = int(input("Please Enter The Number Of Available Watch Models : "))
m = int(input("Please Enter The Number Of Available Phone Cover Models : "))
watches = []
pCovers = []
sumInEachCaseList = []
priceOfWatch = input("Enter a list Of Price Of Watches separated by space: ")
watches = priceOfWatch.split()
for i in range(0, len(watches)):
    watches[i] = int(watches[i])
priceOfPhoneCover = input("Enter a list Of Price Of Phone Covers separated by space: ")
pCovers = priceOfPhoneCover.split()
for j in range(0, len(pCovers)):
    pCovers[j] = int(pCovers[j])
for l in range(0, n):
    for o in range(0, m):
        sumInEachCase = (watches[l] + pCovers[o])
        if sumInEachCase <= b:
            sumInEachCaseList.append(sumInEachCase)
sumInEachCaseList.sort()
try:
    print("Maximum Amount Amol Can Spend Is :", sumInEachCaseList[-1])
except:
    print("Amol Does Not Have Enough Money To Buy 1 Watch And 1 Phone Cover. Hence Value = -1.")
