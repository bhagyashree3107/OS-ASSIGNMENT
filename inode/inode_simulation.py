class Inode:
    def __init__(self, inode_number, filename):
        self.inode_number = inode_number
        self.filename = filename
        self.allocated = True
        self.blocks = []


class FileSystem:
    def __init__(self):
        self.next_inode = 1
        self.inodes = {}
        self.free_blocks = list(range(100, 111))

    # ialloc - allocate a new inode
    def ialloc(self, filename):
        inode_number = self.next_inode
        self.next_inode += 1

        inode = Inode(inode_number, filename)
        self.inodes[filename] = inode

        print(f"ialloc(): Inode {inode_number} allocated for '{filename}'")

        return inode

    # namei - locate inode using filename
    def namei(self, filename):
        print(f"namei(): Searching for '{filename}'")

        if filename in self.inodes:
            inode = self.inodes[filename]
            print(
                f"namei(): Found '{filename}' "
                f"-> Inode {inode.inode_number}"
            )
            return inode

        print(f"namei(): '{filename}' not found")
        return None

    # alloc - allocate disk blocks
    def alloc(self, inode, number_of_blocks):
        print(
            f"alloc(): Allocating {number_of_blocks} "
            f"blocks for Inode {inode.inode_number}"
        )

        if len(self.free_blocks) < number_of_blocks:
            print("alloc(): Not enough free blocks")
            return False

        for _ in range(number_of_blocks):
            block = self.free_blocks.pop(0)
            inode.blocks.append(block)

        print(
            f"alloc(): Blocks allocated -> {inode.blocks}"
        )

        return True

    # free - release disk blocks
    def free(self, inode):
        print(
            f"free(): Releasing blocks "
            f"{inode.blocks}"
        )

        self.free_blocks.extend(inode.blocks)
        self.free_blocks.sort()

        inode.blocks = []

        print(
            f"free(): Free blocks -> {self.free_blocks}"
        )

    # ifree - release inode
    def ifree(self, inode):
        print(
            f"ifree(): Releasing Inode "
            f"{inode.inode_number}"
        )

        inode.allocated = False

        if inode.filename in self.inodes:
            del self.inodes[inode.filename]

        print(
            f"ifree(): Inode {inode.inode_number} released"
        )


# --------------------------------------------------
# Simulation
# --------------------------------------------------

fs = FileSystem()

print("=" * 65)
print("UNIX INODE ALLOCATION AND DEALLOCATION SIMULATION")
print("=" * 65)

print("\nInitial free blocks:")
print(fs.free_blocks)

# -----------------------------------------------
# VM / file creation
# -----------------------------------------------

print("\n--- VM FILE CREATION ---")

inode = fs.ialloc("cloud_vm.img")

fs.namei("cloud_vm.img")

fs.alloc(inode, 5)

print("\nFile created successfully.")

print("\nCurrent inode information:")
print("Inode number :", inode.inode_number)
print("Filename     :", inode.filename)
print("Blocks       :", inode.blocks)
print("Allocated    :", inode.allocated)

# -----------------------------------------------
# File lookup
# -----------------------------------------------

print("\n--- FILE LOOKUP ---")

fs.namei("cloud_vm.img")

# -----------------------------------------------
# VM / file deletion
# -----------------------------------------------

print("\n--- VM FILE DELETION ---")

fs.namei("cloud_vm.img")

fs.free(inode)

fs.ifree(inode)

print("\nFile deleted successfully.")

print("\nFinal free blocks:")
print(fs.free_blocks)

print("\n" + "=" * 65)
print("INODE SIMULATION COMPLETED")
print("=" * 65)