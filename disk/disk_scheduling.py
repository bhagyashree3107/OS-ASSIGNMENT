requests = [86, 147, 312, 91, 177, 48, 409, 22, 130, 365, 220, 480]

initial_head = 125
disk_start = 0
disk_end = 499


def calculate_movement(sequence, head):
    movement = 0

    for position in sequence:
        movement += abs(position - head)
        head = position

    return movement


# -------------------------------------------------
# FCFS
# -------------------------------------------------

def fcfs(requests, head):
    sequence = requests.copy()
    movement = calculate_movement(sequence, head)

    return sequence, movement


# -------------------------------------------------
# SSTF
# -------------------------------------------------

def sstf(requests, head):
    pending = requests.copy()
    sequence = []
    current = head

    while pending:
        nearest = min(
            pending,
            key=lambda request: abs(request - current)
        )

        sequence.append(nearest)
        pending.remove(nearest)
        current = nearest

    movement = calculate_movement(sequence, head)

    return sequence, movement


# -------------------------------------------------
# SCAN
# Direction: Higher cylinders first
# -------------------------------------------------

def scan(requests, head):
    lower = sorted([r for r in requests if r < head])
    higher = sorted([r for r in requests if r >= head])

    sequence = higher + [disk_end] + lower[::-1]

    movement = calculate_movement(sequence, head)

    return sequence, movement


# -------------------------------------------------
# C-SCAN
# Direction: Higher cylinders first
# -------------------------------------------------

def cscan(requests, head):
    lower = sorted([r for r in requests if r < head])
    higher = sorted([r for r in requests if r >= head])

    sequence = higher + [disk_end, disk_start] + lower

    movement = calculate_movement(sequence, head)

    return sequence, movement


# -------------------------------------------------
# LOOK
# Direction: Higher cylinders first
# -------------------------------------------------

def look(requests, head):
    lower = sorted([r for r in requests if r < head])
    higher = sorted([r for r in requests if r >= head])

    sequence = higher + lower[::-1]

    movement = calculate_movement(sequence, head)

    return sequence, movement


# -------------------------------------------------
# Run all algorithms
# -------------------------------------------------

algorithms = {
    "FCFS": fcfs,
    "SSTF": sstf,
    "SCAN": scan,
    "C-SCAN": cscan,
    "LOOK": look
}


print("=" * 75)
print("DISK SCHEDULING ALGORITHM COMPARISON")
print("=" * 75)

print("\nDisk cylinders :", f"{disk_start} - {disk_end}")
print("Initial head   :", initial_head)
print("Direction      : Higher cylinders")
print("Request queue  :", requests)

print("\n" + "-" * 75)
print(f"{'Algorithm':<15}{'Service Sequence':<50}{'Movement':<10}")
print("-" * 75)

for name, algorithm in algorithms.items():

    sequence, movement = algorithm(requests, initial_head)

    print(
        f"{name:<15}"
        f"{str(sequence):<50}"
        f"{movement:<10}"
    )

print("-" * 75)

print("\nAverage Seek Distance:")

for name, algorithm in algorithms.items():

    sequence, movement = algorithm(requests, initial_head)

    average = movement / len(requests)

    print(f"{name:<15}: {average:.2f} cylinders")