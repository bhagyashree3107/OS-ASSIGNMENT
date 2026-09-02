# CloudMatrix Results and Validation

## 1. Memory Management Results

### Physical and Virtual Memory

| Parameter | Value |
|---|---:|
| Physical RAM | 32 GB |
| Page Size | 4 KB |
| Physical Frames | 8,388,608 |
| Logical Address Space | 128 MB |
| Virtual Pages | 32,768 |
| Virtual Address Size | 27 bits |
| Page Offset | 12 bits |

The physical frame count is calculated as:

32 GB / 4 KB = 8,388,608 frames

The logical address space contains:

128 MB / 4 KB = 32,768 pages

Therefore, 15 bits are required to identify a virtual page and 12 bits are required for the page offset.

---

## 2. Page Replacement Results

Reference String:

```text
2, 3, 4, 2, 1, 5, 6, 2, 3, 7, 6, 3, 2, 1, 2, 36