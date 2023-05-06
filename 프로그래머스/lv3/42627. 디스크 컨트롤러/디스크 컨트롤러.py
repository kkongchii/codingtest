import heapq
def solution(jobs):
    # heap = []
    # jobs_num = len(jobs)
    # time = 0
    # wait_time = 0
    # is_running = 0
    # start_time = 0
    # while True:
    #     # print(heap, jobs, time, wait_time, is_running)
    #     # 매 time 마다 해당 time 진입 프로세스 검사
    #     # on_running이 없으면 새 프로세스 진입(시간 가장 짧은 프로세스)
    #     # on_running이 없고, heap, jobs 전부 없으면 프로그램 종료
    #     if jobs and jobs[0][0] == time:
    #         job = jobs.pop(0)
    #         heapq.heappush(heap, (job[1], job[0]))
    #         # input_time.append(time)
    #     if heap:
    #         if is_running:
    #             time += 1
    #             is_running -= 1
    #         else:
    #             wait_time += time - start_time
    #             running_process = heapq.heappop(heap)
    #             is_running = running_process[0]
    #             start_time = running_process[1]
    #             time += 1
    #             is_running -= 1
    #     else:
    #         if is_running:
    #             time += 1
    #             is_running -= 1
    #         else:
    #             if not jobs:
    #                 wait_time += time - start_time
    #                 break
    #             time += 1
    # # 도저히 time 1틱 마다 체크하는건 못하겠다
    start_time = -1
    cur_time = 0
    wait_time = 0
    i = 0
    heap = []
    jobs_num = len(jobs)
    while i < jobs_num:
        for job in jobs:
            if start_time < job[0] <= cur_time:
                heapq.heappush(heap, [job[1], job[0]])
                # 수행시간을 앞에 둬야 이걸 기준으로 힙정렬
        if len(heap) > 0:
            cur_job = heapq.heappop(heap)
            start_time = cur_time
            cur_time += cur_job[0]
            wait_time += cur_time - cur_job[1]
            i += 1
        else:
            cur_time += 1
    
    answer = wait_time // jobs_num
    return answer



# solution([[0, 3], [1,9], [2,6]])