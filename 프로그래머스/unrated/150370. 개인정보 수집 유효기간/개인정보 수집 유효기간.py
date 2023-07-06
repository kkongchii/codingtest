from collections import defaultdict
def solution(today, terms, privacies):
    answer = []
    
    term_dict = defaultdict(int)
    for term in terms:
        term_dict[term[0]] = int(term[2:])
    
    now = int(today[:4])*12*28 + int(today[5:7])*28 + int(today[8:])
    print(term_dict, now)
    
    for i in range(len(privacies)):
        year = int(privacies[i][:4])
        month = int(privacies[i][5:7])
        day = int(privacies[i][8:10])
        
        term = term_dict[privacies[i][-1]]*28
        end = year*12*28 + month*28 + day + term
        
        print(end, now)
        if end <= now:
            answer.append(i+1)
    
    print(answer)
    return answer