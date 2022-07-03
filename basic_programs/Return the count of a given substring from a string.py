string_1 = input("Enter the string to be checked ")
    string_2 = string_1.split()
    checking_string = input("enter string to be checked")
    j = 0
    for i in range(len(string_2)):
        if string_2[i] == checking_string:
            j += 1
    print(checking_string, " Has apperied ", j)
