reference_string = [
    2, 3, 4, 2, 1, 5, 6, 2,
    3, 7, 6, 3, 2, 1, 2, 36
]


def optimal(reference_string, frame_count):
    frames = []
    page_faults = 0
    page_hits = 0

    print(f"\nOPTIMAL - {frame_count} Frames")
    print("=" * 60)

    for i, page in enumerate(reference_string):

        if page in frames:
            page_hits += 1
            result = "HIT"

        else:
            page_faults += 1
            result = "FAULT"

            if len(frames) < frame_count:
                frames.append(page)

            else:
                future = reference_string[i + 1:]

                # Find which page will be used farthest in the future
                next_use = []

                for frame in frames:
                    if frame in future:
                        next_use.append(future.index(frame))
                    else:
                        next_use.append(float("inf"))

                # Replace the page used farthest in the future
                replace_index = next_use.index(max(next_use))
                frames[replace_index] = page

        print(
            f"Reference: {page:>2} | "
            f"Frames: {frames} | "
            f"{result}"
        )

    print("=" * 60)
    print("Total Page Faults:", page_faults)
    print("Total Page Hits  :", page_hits)

    return page_faults, page_hits


optimal(reference_string, 3)
optimal(reference_string, 4)