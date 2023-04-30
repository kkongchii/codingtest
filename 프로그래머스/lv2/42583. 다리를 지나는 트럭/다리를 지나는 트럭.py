def solution(bridge_length, weight, truck_weight):
    time = 0
    total_weight = 0
    truck_on_bridge = []
    
    while True:
        print(truck_weight, truck_on_bridge, total_weight)
        if truck_weight:
            if (total_weight + truck_weight[0]) <= weight:
                total_weight += truck_weight[0]
                time += 1
                truck_on_bridge.append(truck_weight.pop(0))
            else:
                time += bridge_length - min(1,len(truck_on_bridge))
                total_weight -= truck_on_bridge.pop(0)
        else:
            time += bridge_length - len(truck_on_bridge)
            total_weight -= truck_on_bridge.pop(0)
            if not truck_on_bridge:
                break
        print(time)
    
    answer = time
    return answer