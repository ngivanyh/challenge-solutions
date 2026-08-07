"""
You are inputted (sequentially):
    the amount of machines (N) and the amount of workloads (M) to be placed on them
    N lines of each workload, each containing:
        start index, end index, and the amount
        (each machine in that range must do amount work)
    then finally M items, indicating how long it takes for the machine to do
    amount 1

You are free to arrange the machines beforehand to yield
the shortest time to reach the goal
"""

MACHINES, ASSIGNMENTS = map(int, input().split())

WORKLOADS = tuple(tuple(map(int, input().split())) for _ in range(ASSIGNMENTS))
PROCESS_TIMES = tuple(sorted(map(int, input().split())))

workload_diff_arr = [0] * (MACHINES + 1)

for start, end, qty in WORKLOADS:
    workload_diff_arr[start - 1] += qty
    workload_diff_arr[end] -= qty

cur_qty = 0
workload_machines = [0] * MACHINES
for i in range(MACHINES):
    cur_qty += workload_diff_arr[i]
    workload_machines[i] += cur_qty

# ascending order, i.e. most workloads on index i to the least
workload = sorted(workload_machines, key=lambda w: -w)

print(sum(work*time for work, time in zip(workload, PROCESS_TIMES)))