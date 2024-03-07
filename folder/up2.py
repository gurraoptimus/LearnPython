def uppgift2(name, last_name, age):
    ## User input / Användar data
    name = input("Your name/Ditt namn:")
    last_name = input("Your last name/Ditt efternamn:")
    age = input("Your age/Din ålder:")

    ##Överskrider alltid den befintliga informationen
    with open("namelist.txt", "w") as file:
        file.write(f"{name} {last_name},{age}\n")
        file.close

if __name__ == "__main__":
    uppgift2(age)
    