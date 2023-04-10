from collections import Counter

def solution(participant, completion):
    failure = list(set(participant) - set(completion))
    if len(failure) != 0:
        return failure[0]
    else:
        counter = Counter(participant+completion).most_common()
        for member in counter:
            if member[1] % 2 != 0:
                return member[0]