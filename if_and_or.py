#if_and_or.py (EM)
for i in range (1,101):
    if (i%3 == 0 and (i%5 == 0 or i%7 == 0 or i%11 == 0)):
        print(i, " is a multiple of 3 and devisible by, 5,7 or 11")

for j in range (1,101):
    if (j%2 == 0 and j%3 == 0):
        print(j," is divisible by 2 and 3 ")
