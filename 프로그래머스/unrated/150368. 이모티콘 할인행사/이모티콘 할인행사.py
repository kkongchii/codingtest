from itertools import product
# 할인율 -> 4개, 유저 -> 100, 이모티콘 -> 7개, 완탐으로 가볼까, 다른거 생각안남
def solution(users, emoticons):
    answer = []
    # 플러스 가입이 1순위
    sales = list(product([10,20,30,40], repeat=len(emoticons)))
    m_profit = 0
    m_plus_member = 0
    for sale in sales:
        plus_member = 0
        profit = 0
        for user in users:
            price = 0
            for i in range(len(sale)):
                if sale[i] >= user[0]:
                    price += emoticons[i]*(1-sale[i]/100)
            if price>=user[1]:
                plus_member += 1
            else:
                profit += price
        if plus_member > m_plus_member:
            m_plus_member = plus_member
            m_profit = profit
        elif plus_member == m_plus_member:
            m_profit = max(profit, m_profit)
    
    # print(m_plus_member, m_profit)
    answer.append(m_plus_member)
    answer.append(int(m_profit))
        
    return answer