t = int(input())

for _ in range(t):
    string = input().strip()

    string = string.split()


    largest_word = max(len(word) for word in string)

    border = "*"*(largest_word+2)

    print(border)

    for word in string:
        print("*"+word.ljust(largest_word)+"*")
    print(border)

    print("\n\n")