a = int(input("N1: "))
b = int(input("N2: "))
d = []
e = []
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        d.append(i)
for i in d:
    i = str(i)
    if i[::-1]==i:
        e.append(i)
print("there are",len(e),"prime palindrome numbers between",a,"and",b)
c = int(input("n: "))
if c > len(e):
    print("There are not many prime palindrome numbers in the above given range")
else:
    print(e[c-1])
