
# gas station
# https://leetcode.com/problems/gas-station/


def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:

    def mesureGasAtIndexStart(g: list[int], c: list[int], i_start: int) -> bool:
        tank = g[i_start]
        current_station = i_start

        while True:
            if c[current_station] > tank:  # can't road to next station.
                break
            tank -= c[current_station]

            next_station = (current_station + 1) % len(g)  # fill to station dest.
            tank += g[next_station]

            current_station = next_station  # increase station index.

            if current_station == i_start:  # make a loop.
                return True
        
        return False

    
    # try to index.
    for i in range(len(gas)):
        if mesureGasAtIndexStart(gas, cost, i):
            return i

    # no index allow to do a full turn.
    return -1



print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  # 3.
print(canCompleteCircuit([2,3,4], [3,4,3]))  # -1.