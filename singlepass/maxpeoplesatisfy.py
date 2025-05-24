people=[1,6,2,3,4,5]
bundle=[4,2,3,1,1,2]
n=len(people)
people.sort()
bundle.sort()
count=0
i=0
j=0
while i<n and j<n:
    if people[i]<=bundle[j]:
        count+=1
        i+=1
    else:
        j=j+1
print(count)