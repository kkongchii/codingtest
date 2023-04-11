def solution(sizes):
    max1 = 0
    max2 = 0
    for card in sizes:
        if card[0] < card[1]:
            tmp = card[0]
            card[0] = card[1]
            card[1] = tmp
        if card[0] > max1:
            max1 = card[0]
        if card[1] > max2:
            max2 = card[1]
    answer = max1*max2
    return answer