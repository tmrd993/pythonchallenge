import bz2

# username and password are contained in the html doc
rawun = (b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80'
       b'\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084');
rawpw = (b'BZh91AY&SY\x94$|\x0e\x00\x00\x00'
         b'\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08');

decompusername = bz2.decompress(rawun);
decomppassword = bz2.decompress(rawpw);

print('username: ' + decompusername.decode('utf-8'));
print('password: ' + decomppassword.decode('utf-8'));
