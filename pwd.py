import random

pwd="abcdefgijklmnopqrstuvw123456789_%&#*"

ld= input("pwd?:")
ld= int(ld)

password=""
for i in range(ld):
    sl_tk= random.choice(pwd)
    if random.randint(0,1)==0:
        sl_tk=sl_tk.upper()|
    
    password+= sl_tk
print(password)