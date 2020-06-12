# enter number of rows: 10
# A A A A A A A A A A
# B B B B B B B B B B
# C C C C C C C C C C
# D D D D D D D D D D
# E E E E E E E E E E
# F F F F F F F F F F
# G G G G G G G G G G
# H H H H H H H H H H
# I I I I I I I I I I
# J J J J J J J J J J

row = int(input("enter number of rows: "))
for r in range(row):
    for c in range(row):
        print(chr(65+r),end=" ")
    print()
