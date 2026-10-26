# Logical Shift Operations on 8-bit Binary Numbers

def logical_left_shift(binary, positions):
    print("\nLogical Left Shift")
    print("Original number:", binary)

    for i in range(positions):
        binary = binary[1:] + '0'
        print("After shift", i + 1, ":", binary)

    print("Final result:", binary)


def logical_right_shift(binary, positions):
    print("\nLogical Right Shift")
    print("Original number:", binary)

    for i in range(positions):
        binary = '0' + binary[:-1]
        print("After shift", i + 1, ":", binary)

    print("Final result:", binary)


print("LOGICAL SHIFT OPERATIONS")

# (a) Left shift by 2 positions
print("\n(a) Left shift of 10110110 by 2")
logical_left_shift("10110110", 2)

# (b) Right shift by 2 positions
print("\n(b) Right shift of 11010100 by 2")
logical_right_shift("11010100", 2)