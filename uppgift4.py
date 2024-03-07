def belle(numbers):
    # Kollar att numbers är exakt 3 tal
    if len(numbers) != 3:
        return "Listan måste ha tre tal!"

    # Hittar den största siffran
    max_number=max(numbers)
    return max_number

numbers=[94,96,23]
largest_number = belle(numbers)
print("Det största talet är:", largest_number)
