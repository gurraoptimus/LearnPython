name =input("Enter a name:")

#Enter the index of letters (A-1, B-2, etc.) into the file
with open("TxtNameCode.txt","a") as f:
    for letter in name:
        f.write(str(ord(letter)-100) +" ")
    f.write("\n")

#Load and print everything from the file
with open("TxtNameCode.txt","r") as f:
    for line in f.readlines():
        print(line)