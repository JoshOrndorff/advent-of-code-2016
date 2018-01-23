
def is_clock(signal):
    if len(signal) < 2:
        return False

    if signal == "01":
        return True

    if signal[:2] == "01":
        return is_clock(signal[2:])

    return False


def generate_signal(a, b, c):
    output = ""

    a += b * c
    while a != 0:
        b = a % 2
        a = a // 2
        output += str(b)

    return output


########### Main Program #################
'''
print("Testing is_clock")
print(is_clock("01"))
print(is_clock("0101"))
print(is_clock("0101010101"))

print(is_clock(""))
print(is_clock("0"))
print(is_clock("1"))
print(is_clock("110"))
print(is_clock("01010101010"))
print(is_clock("101010"))
'''


# Get puzzle inputs
with open("input.txt", 'r') as f:
    lines = f.read().splitlines()
    b = int(lines[2].split(" ")[1])
    c = int(lines[1].split(" ")[1])

# Test the first thousand a values
for a in range(1000):
    signal = generate_signal(a, b, c)
    if is_clock(signal):
        print(a)
