t = int(input())

for _ in range(t):

    line = input().strip()

    while line == "":
        line = input().strip()

    absent, n = line.split()
    n = int(n)

    all_students = {absent}
    returned_owners = set()

    for _ in range(n):

        transaction = input().split()

        student = transaction[0]
        owner = transaction[3][:-2]

        all_students.add(student)
        all_students.add(owner)

        returned_owners.add(owner)

    missing_owner = (all_students - returned_owners).pop()

    print(f"{absent} HAS {missing_owner}'s BOOK")