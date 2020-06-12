# enter number of rows: 10
# 10 10 10 10 10 10 10 10 10 10
# 09 09 09 09 09 09 09 09 09 09
# 08 08 08 08 08 08 08 08 08 08
# 07 07 07 07 07 07 07 07 07 07
# 06 06 06 06 06 06 06 06 06 06
# 05 05 05 05 05 05 05 05 05 05
# 04 04 04 04 04 04 04 04 04 04
# 03 03 03 03 03 03 03 03 03 03
# 02 02 02 02 02 02 02 02 02 02
# 01 01 01 01 01 01 01 01 01 01

row = int(input("enter number of rows: "))
for r in range(row):
    for c in range(row):
        if row-r < 10 :
            print("0"+str(row-r),end=" ")
        else:
            print(row-r,end=" ")    
    print()