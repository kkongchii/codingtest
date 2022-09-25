def solution():
    name = input()
    number = int(input())
    teamlist = []
    max = -1
    max_i = -1

    for i in range(number):
        teamlist.append(input())
    
    teamlist = sorted(teamlist)
    
    if number==1:
        print(teamlist[0])
    else:
        for i in range(number):
            L = name.count('L')+teamlist[i].count('L')
            O = name.count('O')+teamlist[i].count('O')
            V = name.count('V')+teamlist[i].count('V')
            E = name.count('E')+teamlist[i].count('E')
    
            score = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100
            if score > max:
                max = score
                max_i = i
        print(teamlist[max_i])
    
solution()

    