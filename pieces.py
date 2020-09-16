

def toBinString(hex_data):
    return bin(int(hex_data, 16))[2:].zfill(16)
I = ["0x0F00", "0x2222", "0x00F0", "0x4444"]

print(toBinString(I[0]))
print(toBinString(I[1]))
print(toBinString(I[2]))
print(toBinString(I[3]))