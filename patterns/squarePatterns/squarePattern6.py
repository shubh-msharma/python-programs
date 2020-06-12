# enter number of row: 10
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J

row = int(input("enter number of row: "))
for r in range(row):
    for c in range(row):
        print(chr(65+c),end=" ")
    print()
