import argon2

password1 = input("Enter ur password: ")
# Hash a password using Argon2
password = password1.encode("utf-8")
hasher = argon2.PasswordHasher()
hashed_password = hasher.hash(password)
print(hashed_password)


# Verify a password against its hash
password_attempt = password1.encode("utf-8")
try:
    hasher.verify(hashed_password, password_attempt)
    print("Password is correct!")
except argon2.exceptions.VerifyMismatchError:
    print("Password is incorrect!")

print(len(hashed_password))
