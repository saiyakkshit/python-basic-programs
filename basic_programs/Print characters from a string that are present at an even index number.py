if __name__ == "__main__":
    l = input("Enter a string")
    n = list(l) #conversion of given string into list
    for i in range(len(n)):
        if i % 2 == 0: #print the eventh character in the string
            print(n[i])
