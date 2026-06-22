n = input("Enter your word to check How many vowels it has: ")


vowels = "aeiouAEIOU"

count = 0

for char in n:
    if char in vowels:
        count += 1
print("Number of vowels in the word is:", count)