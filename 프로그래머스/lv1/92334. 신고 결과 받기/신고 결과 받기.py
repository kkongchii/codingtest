from collections import defaultdict

def solution(id_list, report, k):
    # 코테 공부 이전에 풀었던 풀이, 정답이긴함
#     s = set(report)
#     report = list(s)
#     reportdic = {}
#     maildic = {}
#     answer = [0]*len(id_list)

#     for name in id_list:
#         reportdic[name] = 0
#         maildic[name] = 0
    
#     for reportstr in report:
#         tmp = reportstr.split(" ")
#         reportdic[tmp[1]] = reportdic[tmp[1]] + 1
    
#     for reportstr in report:
#         tmp = reportstr.split(" ")
#         if reportdic[tmp[1]] >= k:
#             maildic[tmp[0]] = maildic[tmp[0]] + 1
    
#     for i in range(len(id_list)):
#         answer[i] = maildic[id_list[i]]

    users = defaultdict(list)
    answer = [0]*len(id_list)
    
    for case in report:
        reporter = (case.split(" "))[0]
        reportee = (case.split(" "))[1]
        if reporter not in users[reportee]:
            users[reportee].append(reporter)
            
    for user in users.keys():
        if len(users[user]) >= k:
            for mail in users[user]:
                answer[id_list.index(mail)] += 1
    
    return answer