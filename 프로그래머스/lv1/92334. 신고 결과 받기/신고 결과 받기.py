def solution(id_list, report, k):
    s = set(report)
    report = list(s)
    reportdic = {}
    maildic = {}
    answer = [0]*len(id_list)

    for name in id_list:
        reportdic[name] = 0
        maildic[name] = 0
    
    for reportstr in report:
        tmp = reportstr.split(" ")
        reportdic[tmp[1]] = reportdic[tmp[1]] + 1
    
    for reportstr in report:
        tmp = reportstr.split(" ")
        if reportdic[tmp[1]] >= k:
            maildic[tmp[0]] = maildic[tmp[0]] + 1
    
    for i in range(len(id_list)):
        answer[i] = maildic[id_list[i]]
                
    return answer