import random

pwd = "abcdefgijklmnopqrstuvw123456789_%&#*"

ld = input("How long do you want the password to be?: ")
ld = int(ld)

passwd = ""
for i in range(ld):
    sl_tk = random.choice(pwd)
    
    if random.randint(0, 1) == 0:
        sl_tk = sl_tk.upper()

    passwd += sl_tk

print("Your generated password is:", passwd)
