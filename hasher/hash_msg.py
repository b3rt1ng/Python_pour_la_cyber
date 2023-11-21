import hashlib

m=input("Enter the message: ")

sha1=hashlib.sha1(m.encode())
sha256=hashlib.sha256(m.encode())
sha512=hashlib.sha512(m.encode())
md5=hashlib.md5(m.encode())
blake2b=hashlib.blake2b(m.encode())

print(f"{m} -> {sha1.hexdigest()} (sha1)")
print(f"{m} -> {sha256.hexdigest()} (sha256)")
print(f"{m} -> {sha512.hexdigest()} (sha512)")
print(f"{m} -> {md5.hexdigest()} (md5)")
print(f"{m} -> {blake2b.hexdigest()} (blake2b)")