import zlib
s = b'witch which has which witches wrist watch'
len(s)
41 #output
t = zlib.compress(s)
len(t)
37 #output
zlib.decompress(t)
b'witch which has which witches wrist watch' #output
zlib.crc32(s)
226805979 #output