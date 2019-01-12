print("Anas Ahmed")
print("(18B-116-CS),Sec-A")
print("Practice Problem 3.40")
def partition(names):
    return[firstname for firstname in names
           if firstname[0].lower() in 'abcdefghijklm']

x = partition(['Hassan','Sarim', 'Yusra','Rushan'])
x.sort()
print(*x,sep = '\n')
