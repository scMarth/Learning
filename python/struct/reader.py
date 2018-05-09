import struct

with open("./data.dat") as file:
   file.seek(0)
   data = file.read(8)
   print(data)

   file.seek(0)
   values = struct.unpack(">4s2sBB", file.read(8))
   print("")
   print(len(values))
   print("")
   print(values[0]) # s = char[] ; string
   print(values[1]) # s = char[] ; string
   print(values[2]) # B = unsigned char ; integer
   print(values[3]) # B = unsigned char ; integer

   print("i = 105 in decimal in ascii table")
   print("c = 99 in decimal in ascii table")

   print("")
   file.seek(0)
   print(file.read(1)[0])