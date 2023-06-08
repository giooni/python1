usernames = ["Nick", "Theo", "Theodor", "Mary", "nana", "manana"]
upper = [
    names.upper()
    for names in usernames
]

new  = usernames[:3]



alpha = 'abcdefghijqlmopqrstuvwxyz'

def search(x, y,z):
    in1 = alpha.find(x)
    in2 = alpha.find(y)
    in3 = alpha.find(z)
    maxval = max(in1, in2, in3)
    minval = min(in1, in2, in3)
    return alpha[minval:maxval+1]

users = [
["Legend27", "a1s2d3f4"],
["james123", "c5bt43f4"],
["DaveIsGreat", "wlervtb3r"]
]

balances = [
150000,
12000,
19000
]


for i in range(len(users)):
    users[i].append(balances[i])




prime = []

i = 1000
for j in range(2, 100000):
    is_prime = True
    for k in range(2, int(j/2) + 1):
        if j % k == 0:
            is_prime = False
            
    if i ==0:
        break        
    if is_prime and i>0:
        prime.append(j)
        i-=1
        




lst = ["a" , 11, 21, 13, "b"]
for i in range(len(lst)):
    print(lst[i])


for i in range(len(lst)):
     if i%2==1:
         print(lst[i])

"""
bonus
"""

a =  input()
if a.isnumeric():


    num  = str(a)
    if int(num[len(num)-1])%2==0:
        print(num + " " + "is even")
    else:
        print(num + " "+ "is odd")
else:
    print("invalid value")