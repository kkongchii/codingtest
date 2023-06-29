n = int(input())
money = [0] * (n+1)  # 0부터 n까지의 인덱스를 사용하기 위해 크기를 n+1로 설정
time = [0]  # 인덱스 1부터 사용하기 위해 0 추가
pay = [0]  # 인덱스 1부터 사용하기 위해 0 추가

for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

for i in range(1, n+1):
    if i + time[i] <= n + 1:
        money[i] = pay[i]  # 당일 페이
        for j in range(1, i):  # 이전에 완료한 상담만 확인하도록 수정
            if j + time[j] <= i:
                money[i] = max(money[i], pay[i] + money[j])

print(max(money))
