def crc32(crc, p, len):
  crc = 0xffffffff & ~crc
  for i in range(len):
    crc = crc ^ p[i]
    for j in range(8):
      crc = (crc >> 1) ^ (0xedb88320 & -(crc & 1))
  return 0xffffffff & ~crc

def cr(s):
    return hex(crc32(0, s.encode("ascii"), len(s)))

desired = "<script src=\"https://67.194.201.116"

#len < 128
