board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)
    
else:
    print(board)
//출처: https://s0ng.tistory.com/entry/백준-그리디-알고리즘-폴리오미노-1343번-파이썬-python [S0NG의 정보보안 블로그:티스토리]
