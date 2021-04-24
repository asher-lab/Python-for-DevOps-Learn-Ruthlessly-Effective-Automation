import hashlib
secret= "This is a confidential document"
bsecret=secret.encode()
#Using md5 algorithm
m=hashlib.md5()
m.update(bsecret)
print(m.digest)
