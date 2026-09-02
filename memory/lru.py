reference_string = [
    2, 3, 4, 2, 1, 5, 6, 2,
    3, 7, 6, 3, 2, 1, 2, 36
]


def lru(reference_string, frame_count):
    frames = []
    page_faults = 0
    page_hits = 0

    print(f"\nLRU - {frame_count} Frames")
    print("=" * 60)

    for page in reference_string:

        if page in frames:
            page_hits += 1
            result = "HIT"

            # Move recently used page to the end
            frames.remove(page)
            frames.append(page)

        else:
            page_faults += 1
            result = "FAULT"

            if len(frames) < frame_count:
                frames.append(page)
            else:
                # Remove least recently used page
                frames.pop(0)
                frames.append(page)

        print(
            f"Reference: {page:>2} | "
            f"Frames: {frames} | "
            f"{result}"
        )

    print("=" * 60)
    print("Total Page Faults:", page_faults)
    print("Total Page Hits  :", page_hits)

    return page_faults, page_hits


lru(reference_string, 3)
lru(reference_string, 4)