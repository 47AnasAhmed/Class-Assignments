print("Anas Ahmed")
print("(18B-116-CS),Sec-A")
print("Practice Problem 3.10")
def novowel(x):
    for i in x:
        if i in "aeiouAEIOU":
            return False
    return True
v = novowel('python')
print(v)
