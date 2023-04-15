def solution(phone_book):
    # min_len_number = phone_book[0]
    # count = 0
    # for number in phone_book:
    #     if len(number) < len(min_len_number):
    #         min_len_number = number
    # for number in phone_book:
    #     if number[:len(min_len_number)] == min_len_number:
    #         count = count+1
    # print(count)
    # if count>1:
    #     answer = False
    # else:
    #     answer = True
    # return answer
    # 최단 길이의 전화번호만 항상 접두어에 해당되지 않음, 시간초과
    
    # sorted_book = sorted(phone_book)
    # for i in range(len(sorted_book)):
    #     for j in range(i+1,len(sorted_book)):
    #         if sorted_book[j].startswith(sorted_book[i]):
    #             return False
    # return True
    # 다 통과는 하는데 시간초과에 걸림.. 어떻게 시간을 줄이지?
    
    sorted_book = sorted(phone_book)
    for i in range(len(sorted_book)-1):
        if sorted_book[i+1].startswith(sorted_book[i]):
            return False
    return True