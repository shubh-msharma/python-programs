# enter number of rows: 10
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *
# * * * * * * * * * *
row = int(input("enter number of rows: "))
r = 0
while(r<row):
    c = 0
    while(c<=r):
        print("*",end=" ")
        c += 1
    print()
    r += 1