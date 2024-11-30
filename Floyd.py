num_of_rows=int(input("Please eneter the amount of rows"))

num=1
for i in range(num_of_rows):
    for j in range(i+1):
        print(num,end=" ")
        num=num+1
    print()


    