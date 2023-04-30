from collections import Counter

def solution(genres, plays):
    answer = []
    total_plays = {}
    popular_genres = []
    
    for genre in set(genres):
        total_plays[genre] = 0
    for genre, play in zip(genres, plays):
        total_plays[genre] += play
        
    sorted_genres = sorted(total_plays.items(), key = lambda item: item[1], reverse = True)
    for i in sorted_genres:
        popular_genres.append(i[0])
    
    for i in popular_genres:
        genres_plays = list(filter(lambda x: genres[x] == i, range(len(genres))))

        tmp = []
        for j in genres_plays:
            tmp.append(plays[j])

        max_index = plays.index(max(tmp))
        answer.append(max_index)
        plays[max_index] = -1
        tmp[tmp.index(max(tmp))] = -1
        if len(tmp) > 1:
            answer.append(plays.index(max(tmp)))
        
        
    return answer