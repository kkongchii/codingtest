# 반갑괄호
# 열린괄호는 +1, 닫힌괄호는 -1 해서
# 균형잡힌문자열 :  먼저 0이 될 때 stop
# 올바른문자열 :  문자열 종료까지 음수가 되지 않고 최종적으로 0일때

def balanceBracket(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] =='(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i+1
    

def isRightBracket(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] =='(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    if cnt == 0:
        return True
    else:
        return False
    
def reverseBracket(s):
    string = ''
    for i in range(1, len(s)-1):
        if s[i] == '(':
            string += ')'
        else:
            string += '('
    return string
    
def transformBracket(s):
    
    if s == '':
        return ''
    idx = balanceBracket(s)
    u = s[:idx]
    v = s[idx:]
    # print("u : ", u)
    # print("v : ", v)
    
    if isRightBracket(u):
        return u + transformBracket(v)
    else:
        return '(' + transformBracket(v) + ')' + reverseBracket(u)

def solution(p):
    answer = transformBracket(p)

    return answer