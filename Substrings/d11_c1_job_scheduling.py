# correct code
m1 = [0,6,3,8,1,4,7,9]
m2 = [5,7,5,10,2,7,9,11]

t = []
for i in range(len(m1)):
    t.append([m1[i],m2[i]])

t = sorted(t,key = lambda x: x[1])
print(t)

res = 0
prev_end_time = -1
for time in t:
    if time[0]>prev_end_time:
        print(time[0],":",time[1])
        res += 1
        prev_end_time = time[1]

print("maximum number of meetings we can perform: ",res)