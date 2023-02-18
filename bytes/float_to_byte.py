import struct

value = 435634766785.1123432

ba = bytearray(struct.pack("f", value))

print(ba)
print(type(ba))

for b in ba:
    print(b)
    print(type(b))


print([ "0x%02x" % b for b in ba ])
