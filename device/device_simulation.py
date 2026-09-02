class BlockDevice:
    def __init__(self, name):
        self.name = name
        self.storage = []

    def read(self, block):
        print(f"[BLOCK] Reading block {block} from {self.name}")

    def write(self, block, data):
        print(
            f"[BLOCK] Writing '{data}' "
            f"to block {block} on {self.name}"
        )


class CharacterDevice:
    def __init__(self, name):
        self.name = name

    def read(self):
        print(f"[CHARACTER] Reading character from {self.name}")

    def write(self, data):
        print(
            f"[CHARACTER] Writing '{data}' "
            f"to {self.name}"
        )


# -------------------------------------------------
# Device Driver Tables
# Similar concept to bdevsw / cdevsw
# -------------------------------------------------

bdevsw = {
    "disk0": {
        "driver": "disk_driver",
        "operations": ["read_block", "write_block"]
    },
    "vm_disk": {
        "driver": "virtual_disk_driver",
        "operations": ["read_block", "write_block"]
    }
}


cdevsw = {
    "terminal": {
        "driver": "terminal_driver",
        "operations": ["read_char", "write_char"]
    },
    "console": {
        "driver": "console_driver",
        "operations": ["read_char", "write_char"]
    }
}


print("=" * 70)
print("DEVICE DRIVER AND DEVICE TABLE SIMULATION")
print("=" * 70)


# -------------------------------------------------
# Block Device
# -------------------------------------------------

print("\n--- BLOCK DEVICE ---")

disk = BlockDevice("disk0")

disk.write(10, "VM DATA")
disk.read(10)


# -------------------------------------------------
# Character Device
# -------------------------------------------------

print("\n--- CHARACTER DEVICE ---")

terminal = CharacterDevice("terminal")

terminal.write("Hello CloudMatrix")
terminal.read()


# -------------------------------------------------
# bdevsw
# -------------------------------------------------

print("\n--- BDEVSW TABLE ---")

for device, information in bdevsw.items():
    print(f"Device : {device}")
    print(f"Driver : {information['driver']}")
    print(f"Operations : {information['operations']}")
    print()


# -------------------------------------------------
# cdevsw
# -------------------------------------------------

print("--- CDEVSW TABLE ---")

for device, information in cdevsw.items():
    print(f"Device : {device}")
    print(f"Driver : {information['driver']}")
    print(f"Operations : {information['operations']}")
    print()


# -------------------------------------------------
# Comparison
# -------------------------------------------------

print("--- DEVICE COMPARISON ---")

print("Block Device:")
print("- Transfers data in blocks")
print("- Used for disks and storage devices")
print("- Supports random access")

print("\nCharacter Device:")
print("- Transfers data character by character")
print("- Used for terminals and consoles")
print("- Generally provides sequential access")

print("\n" + "=" * 70)
print("DEVICE SIMULATION COMPLETED")
print("=" * 70)