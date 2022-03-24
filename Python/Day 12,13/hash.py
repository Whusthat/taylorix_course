from passlib.hash import pbkdf2_sha256, argon2

# pw in plaintext
pw = 'Im the greatest'
# hashed pw
pwhash = pbkdf2_sha256.hash(pw)
pwhash2 = pbkdf2_sha256.hash(pw)

print(f'{pwhash} : {pbkdf2_sha256.verify(pw, pwhash)}')
print(f'{pwhash2} : {pbkdf2_sha256.verify(pw,pwhash2)}')



