# * * * * * * * * * *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# * * * * * * * * * *

rNc = int(input("enter number of rows: "))
for r in range(rNc):
    # print(r,end=" ")
    for c in range(rNc):
        if r == 0 or r == rNc-1:
            print("*" , end = " ")
        elif c == 0 or c == rNc-1 :
            print("*" , end = " ")
        else :
            print(" ",end=" ")
    print()
