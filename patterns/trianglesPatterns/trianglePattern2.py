# enter number of rows: 10
# 01
# 02 02
# 03 03 03
# 04 04 04 04
# 05 05 05 05 05
# 06 06 06 06 06 06
# 07 07 07 07 07 07 07
# 08 08 08 08 08 08 08 08
# 09 09 09 09 09 09 09 09 09
# 10 10 10 10 10 10 10 10 10 10

# enter number of rows: 6
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6

row = int(input("enter number of rows: "))
r = 1
while(r < row+1):
    c = 1
    while(c <= r):
        if row < 10 :
            print(r,end=" ")
        else:
            if r < 10:
                print("0"+str(r),end=" ")
            else:
                print(r,end=" ")
        c += 1
    print()
    r += 1
