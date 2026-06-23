n = int(input("Enter the no. of DNA: "))

dna = {
    "A":"T",
    "T":"A",
    "C":"G",
    "G":"C"
}
result = ""
for i in range(n):
    base = input().strip()

    for b in base:
        result += dna[b]
    result +="\n"
print(result)