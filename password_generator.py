import random
print("Welcome to Password Generator!")
capital_letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small_letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_char=["+","*","%","(",")","&","$","#","!"]
numbers=['0','1','2','3','4','5','6','7','8','9']
capital_letters_count=int(input("How many capital letters you want in your password?\n"))
small_letters_count=int(input("How many small letters you want in your password?\n"))
symbols_count=int(input("How many special characters you want in your password?\n"))
numbers_count=int(input("How many numbers you want in your password?\n"))
s=[]
for i in range(1,capital_letters_count+1):
    char=random.choice(capital_letters)
    s+=char
for i in range(1,small_letters_count+1):
    char=random.choice(small_letters)
    s+=char
for i in range(1,symbols_count+1):
    sy=random.choice(special_char)
    s+=sy
for i in range(1,numbers_count+1):
    n=random.choice(numbers)
    s+=n
random.shuffle(s)
password=""
for i in s:
    password+=i
print(password)