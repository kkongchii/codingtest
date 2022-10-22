N = int(input())

for case in range(N):
    M = int(input())
    students = []
    for i in range(M):
        students.append(int(input()))
    for m in range(1,999999):
        remainder = list(map(lambda x : x%m, students))
        if M == len(set(remainder)):
            print(m)
            break
        