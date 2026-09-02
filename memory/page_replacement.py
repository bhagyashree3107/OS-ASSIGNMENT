reference_string = [
    2, 3, 4, 2, 1, 5, 6, 2,
    3, 7, 6, 3, 2, 1, 2, 36
]


def fifo(reference_string, frame_count):
    frames = []
    faults = 0
    pointer = 0

    for page in reference_string:
        if page not in frames:
            faults += 1

            if len(frames) < frame_count:
                frames.append(page)
            else:
                frames[pointer] = page
                pointer = (pointer + 1) % frame_count

    return faults


def lru(reference_string, frame_count):
    frames = []
    faults = 0

    for page in reference_string:
        if page in frames:
            frames.remove(page)
            frames.append(page)
        else:
            faults += 1

            if len(frames) < frame_count:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)

    return faults


def optimal(reference_string, frame_count):
    frames = []
    faults = 0

    for i, page in enumerate(reference_string):

        if page in frames:
            continue

        faults += 1

        if len(frames) < frame_count:
            frames.append(page)
            continue

        future = reference_string[i + 1:]

        next_use = []

        for frame in frames:
            if frame in future:
                next_use.append(future.index(frame))
            else:
                next_use.append(float("inf"))

        replace_index = next_use.index(max(next_use))
        frames[replace_index] = page

    return faults


print("=" * 65)
print("PAGE REPLACEMENT ALGORITHM COMPARISON")
print("=" * 65)

print("\nReference String:")
print(reference_string)

print("\nResults:")
print("-" * 65)
print(f"{'Algorithm':<15}{'3 Frames':<15}{'4 Frames':<15}")
print("-" * 65)

fifo_3 = fifo(reference_string, 3)
fifo_4 = fifo(reference_string, 4)

lru_3 = lru(reference_string, 3)
lru_4 = lru(reference_string, 4)

optimal_3 = optimal(reference_string, 3)
optimal_4 = optimal(reference_string, 4)

print(f"{'FIFO':<15}{fifo_3:<15}{fifo_4:<15}")
print(f"{'LRU':<15}{lru_3:<15}{lru_4:<15}")
print(f"{'Optimal':<15}{optimal_3:<15}{optimal_4:<15}")

print("-" * 65)

print("\nBelady's Anomaly:")
if fifo_4 > fifo_3:
    print("Belady's anomaly occurs in FIFO.")
else:
    print("Belady's anomaly does NOT occur for this reference string.")

print("\nBest Algorithm:")
print("Optimal gives the minimum number of page faults.")