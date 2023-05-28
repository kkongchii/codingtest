# 100명 4500개? 걍 테이블 만들면 되지 않나
# def solution(n, results):
#     answer = 0
#     score = [[0]*(n+1) for _ in range(n+1)]
#     for result in results:
#         score[result[0]] = result[1]
    
    # 승패 테이블을 만들어 봤는데 접근 법이 애매하다.
    # k번째 선수가 이긴 선수와 진 선수 명단을 작성해볼까
    # 다음 선수 결과를 가져와서 모든 선수의 우열을 갱신
    # 근데 이거 for문 엄청 중첩될 것 같은데 흠
    
# def solution(n, results):
#     answer = 0
#     win = [set() for _ in range(n+1)]
#     lose = [set() for _ in range(n+1)]
#     for result in results:
#         win[result[0]].add(result[1])
#         lose[result[1]].add(result[0])
#         for i in lose[result[0]]:
#             win[i].add(result[1])
#             lose[result[1]].add(i)
#         for j in win[result[1]]:
#             lose[j].add(result[0])
#             win[result[0]].add(j)
#         print(win)
#         print(lose, '\n')
    
#     for i in range(n+1):
#         if len(win[i])+len(lose[i]) == n-1:
#             answer += 1
    
#     return answer

# 이것도 안됨, win/lose를 순서를 정해서 갱신하다보니 업데이트가 제대로 안됨

def solution(n, results):
    answer = 0
    win = [set() for _ in range(n+1)]
    lose = [set() for _ in range(n+1)]
    for result in results:
        win[result[0]].add(result[1])
        lose[result[1]].add(result[0])
    print(win)
    print(lose, '\n')
    
    for i in range(1, n+1):
        # i 선수를 이긴 선수들은 i 선수가 이긴 선수들도 이긴다
        for winner in lose[i]:
            win[winner].update(win[i])
        # i 선수에게 진 선수들은 i 선수가 진 선수들에게도 진다
        for loser in win[i]:
            lose[loser].update(lose[i])
    print(win)
    print(lose, '\n')
    
    for i in range(n+1):
        if len(win[i])+len(lose[i]) == n-1:
            answer += 1
    
    return answer

# 마지막에 한번만 업데이트 돌려주면 되더라