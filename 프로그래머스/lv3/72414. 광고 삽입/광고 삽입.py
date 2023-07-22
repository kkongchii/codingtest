# 자 부분합 다시 풀어보자이, 누적합은 기본적으로 dp라고 한다
# 100시간은 대충 36만초 정도 됨 초로 변환하자

def getSecond(time):
    h = int(time[:2])
    m = int(time[3:5])
    s = int(time[6:8])
    return h*60*60 + m*60 + s

def solution(play_time, adv_time, logs):
    answer = ''
    totalPlay = getSecond(play_time)
    totalAd = getSecond(adv_time)
    timeline = [0]*(totalPlay+1)
    for log in logs:
        timeline[getSecond(log[:8])] += 1
        timeline[getSecond(log[-8:])] -= 1
    for i in range(1, len(timeline)): # 총 시청자
        timeline[i] += timeline[i-1]
    for i in range(1, len(timeline)): # 누적 시청자
        timeline[i] += timeline[i-1]
        
    maxWatch = 0
    for i in range(1, totalPlay-totalAd+1):
        partSum = timeline[i+totalAd-1]-timeline[i-1]
        if partSum > timeline[maxWatch+totalAd-1]-timeline[max(0, maxWatch-1)]:
            maxWatch = i
    
    print(maxWatch)
    answer = '{:02d}:{:02d}:{:02d}'.format(maxWatch//3600, maxWatch%3600//60, maxWatch%60)
    return answer